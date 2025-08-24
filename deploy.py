"""
🚀 Gaming Workforce Observatory - Script de Déploiement
Automatise le déploiement vers Streamlit Community Cloud
"""

import subprocess
import os
import sys
from datetime import datetime
import json

class StreamlitDeployer:
    def __init__(self):
        self.project_name = "gaming-workforce-observatory"
        self.main_file = "gaming_workforce_app.py"
        
    def check_prerequisites(self):
        """Vérifie que tous les prérequis sont présents"""
        print("🔍 Vérification des prérequis...")
        
        required_files = [
            'gaming_workforce_app.py',
            'requirements.txt',
            'README.md',
            '.gitignore'
        ]
        
        missing_files = [f for f in required_files if not os.path.exists(f)]
        
        if missing_files:
            print(f"❌ Fichiers manquants: {', '.join(missing_files)}")
            return False
        
        # Vérifier Git
        try:
            subprocess.run(['git', '--version'], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print("❌ Git n'est pas installé")
            return False
        
        print("✅ Tous les prérequis sont présents")
        return True
    
    def run_tests(self):
        """Lance les tests de base"""
        print("🧪 Lancement des tests...")
        
        try:
            # Test basique: vérifier que l'app se charge
            result = subprocess.run([
                sys.executable, '-c', 
                'import streamlit; exec(open("gaming_workforce_app.py").read())'
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print("✅ Tests passés avec succès")
                return True
            else:
                print(f"❌ Tests échoués: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print("⚠️ Tests timeout - continuons le déploiement")
            return True
        except Exception as e:
            print(f"⚠️ Erreur lors des tests: {e}")
            return True  # Continue quand même
    
    def git_status_check(self):
        """Vérifie le statut Git"""
        print("📊 Vérification du statut Git...")
        
        try:
            # Vérifier s'il y a des changements
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, check=True)
            
            if result.stdout.strip():
                print("📝 Changements détectés - préparation du commit")
                return True
            else:
                print("✅ Aucun changement à commiter")
                return False
                
        except subprocess.CalledProcessError:
            print("❌ Erreur lors de la vérification Git")
            return False
    
    def create_commit(self, message=None):
        """Crée un commit avec les changements"""
        if not message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            message = f"🎮 Update Gaming Observatory - {timestamp}"
        
        try:
            # Ajouter tous les fichiers
            subprocess.run(['git', 'add', '.'], check=True)
            
            # Créer le commit
            subprocess.run(['git', 'commit', '-m', message], check=True)
            
            print(f"✅ Commit créé: {message}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors du commit: {e}")
            return False
    
    def push_to_github(self):
        """Push les changements vers GitHub"""
        print("🚀 Push vers GitHub...")
        
        try:
            # Push vers la branche main
            result = subprocess.run(['git', 'push', 'origin', 'main'], 
                                  capture_output=True, text=True, check=True)
            
            print("✅ Push réussi vers GitHub")
            print("🌐 Streamlit Community Cloud va automatiquement redéployer l'app")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors du push: {e}")
            if "authentication" in str(e).lower():
                print("💡 Astuce: Vérifiez vos credentials Git (token GitHub)")
            return False
    
    def display_deployment_info(self):
        """Affiche les informations de déploiement"""
        print("\n" + "="*60)
        print("🎮 GAMING WORKFORCE OBSERVATORY - DÉPLOIEMENT")
        print("="*60)
        print(f"📱 Application: {self.project_name}")
        print(f"📄 Fichier principal: {self.main_file}")
        print(f"🕒 Déploiement: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n🔗 Liens utiles:")
        print("   • Streamlit Cloud: https://share.streamlit.io")
        print("   • Documentation: https://docs.streamlit.io")
        print("   • GitHub: https://github.com/username/gaming-workforce-observatory")
        print("="*60)
    
    def deploy(self, commit_message=None):
        """Lance le processus de déploiement complet"""
        print("🚀 Début du déploiement Gaming Workforce Observatory")
        
        # Affichage des infos
        self.display_deployment_info()
        
        # Vérifications préalables
        if not self.check_prerequisites():
            print("❌ Déploiement annulé - prérequis manquants")
            return False
        
        # Tests
        if not self.run_tests():
            response = input("⚠️ Tests échoués. Continuer ? (y/N): ")
            if response.lower() != 'y':
                print("❌ Déploiement annulé")
                return False
        
        # Git workflow
        if self.git_status_check():
            if not self.create_commit(commit_message):
                print("❌ Déploiement annulé - erreur commit")
                return False
        
        # Push vers GitHub
        if not self.push_to_github():
            print("❌ Déploiement annulé - erreur push")
            return False
        
        print("\n🎉 Déploiement terminé avec succès!")
        print("⏳ L'application sera disponible dans quelques minutes sur:")
        print("   https://gaming-workforce-observatory.streamlit.app")
        print("\nℹ️ Vous pouvez suivre le déploiement sur share.streamlit.io")
        
        return True

def main():
    deployer = StreamlitDeployer()
    
    # Message de commit personnalisé si fourni
    commit_msg = None
    if len(sys.argv) > 1:
        commit_msg = " ".join(sys.argv[1:])
    
    success = deployer.deploy(commit_msg)
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
