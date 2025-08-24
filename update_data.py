"""
🔄 Gaming Workforce Observatory - Mise à jour des Données
Met à jour les données depuis les sources externes
"""

import pandas as pd
import requests
import json
from datetime import datetime
import os

class DataUpdater:
    def __init__(self):
        self.base_url = "https://api.example.com"  # API fictive
        self.last_update = datetime.now()
        
    def fetch_salary_trends(self):
        """Récupère les dernières tendances salariales"""
        print("📈 Mise à jour des tendances salariales...")
        
        # Simulation d'appel API
        try:
            # En production, remplacer par vraies APIs:
            # - LinkedIn Talent Insights
            # - Glassdoor API  
            # - Indeed API
            
            # Pour le moment, on charge les données existantes et on les met à jour
            if os.path.exists('gaming_salaries.csv'):
                df = pd.read_csv('gaming_salaries.csv')
                
                # Simulation d'une augmentation annuelle de 5%
                df['gaming_salary_usd'] = df['gaming_salary_usd'] * 1.05
                df['tech_salary_usd'] = df['tech_salary_usd'] * 1.03
                
                df.to_csv('gaming_salaries.csv', index=False)
                print("✅ Données salaires mises à jour (+5% gaming, +3% tech)")
                
        except Exception as e:
            print(f"❌ Erreur mise à jour salaires: {e}")
    
    def fetch_studio_metrics(self):
        """Met à jour les métriques des studios"""
        print("🏢 Mise à jour des métriques studios...")
        
        try:
            if os.path.exists('global_studios.csv'):
                df = pd.read_csv('global_studios.csv')
                
                # Simulation de fluctuations réalistes
                df['retention_rate'] = df['retention_rate'] + np.random.randint(-2, 3, len(df))
                df['retention_rate'] = df['retention_rate'].clip(60, 95)
                
                # Quelques studios augmentent leurs effectifs
                growth_mask = np.random.choice([True, False], len(df), p=[0.3, 0.7])
                df.loc[growth_mask, 'employees'] *= np.random.uniform(1.02, 1.15, growth_mask.sum())
                df['employees'] = df['employees'].astype(int)
                
                df.to_csv('global_studios.csv', index=False)
                print("✅ Métriques studios mises à jour")
                
        except Exception as e:
            print(f"❌ Erreur mise à jour studios: {e}")
    
    def validate_data(self):
        """Valide l'intégrité des données"""
        print("🔍 Validation de l'intégrité des données...")
        
        issues = []
        
        # Vérification salaires
        if os.path.exists('gaming_salaries.csv'):
            df = pd.read_csv('gaming_salaries.csv')
            if df['gaming_salary_usd'].min() < 20000 or df['gaming_salary_usd'].max() > 500000:
                issues.append("Salaires gaming hors plage réaliste")
            if df.isnull().any().any():
                issues.append("Valeurs manquantes dans données salaires")
        
        # Vérification studios
        if os.path.exists('global_studios.csv'):
            df = pd.read_csv('global_studios.csv')
            if df['retention_rate'].min() < 50 or df['retention_rate'].max() > 100:
                issues.append("Taux de rétention incohérents")
        
        if issues:
            print("⚠️ Problèmes détectés:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print("✅ Données validées - Aucun problème détecté")
        
        return len(issues) == 0
    
    def create_backup(self):
        """Crée une sauvegarde des données actuelles"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_files = ['gaming_salaries.csv', 'global_studios.csv', 'neurodiversity_roi.csv']
        
        for file in backup_files:
            if os.path.exists(file):
                backup_name = f"{file.split('.')[0]}_backup_{timestamp}.csv"
                df = pd.read_csv(file)
                df.to_csv(backup_name, index=False)
        
        print(f"💾 Sauvegarde créée - {timestamp}")
    
    def update_all(self):
        """Lance la mise à jour complète"""
        print("🚀 Début mise à jour Gaming Workforce Observatory")
        print("=" * 50)
        
        # Sauvegarde avant mise à jour
        self.create_backup()
        
        # Mises à jour
        self.fetch_salary_trends()
        self.fetch_studio_metrics()
        
        # Validation
        if self.validate_data():
            print("\n✅ Mise à jour complétée avec succès!")
        else:
            print("\n⚠️ Mise à jour terminée avec des avertissements")
        
        print("=" * 50)

if __name__ == "__main__":
    updater = DataUpdater()
    updater.update_all()
