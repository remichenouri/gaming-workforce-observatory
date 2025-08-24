"""
🎮 Gaming Workforce Observatory - Générateur de Données
Génère des données réalistes pour tests et développement
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import random

class GamingDataGenerator:
    def __init__(self):
        self.seed = 42
        np.random.seed(self.seed)
        random.seed(self.seed)
        
        # Données de base réalistes
        self.game_roles = [
            'Game Developer', 'Game Designer', 'Technical Artist', 
            'Game Producer', 'QA Tester', 'Audio Engineer',
            'UI/UX Designer', 'Game Animator', 'Level Designer'
        ]
        
        self.tech_companies = [
            'Google', 'Meta', 'Amazon', 'Microsoft', 'Apple',
            'Netflix', 'Uber', 'Airbnb', 'Spotify', 'Adobe'
        ]
        
        self.gaming_studios = [
            'Microsoft Gaming', 'Ubisoft', 'Electronic Arts', 'Sony Interactive',
            'Take-Two Interactive', 'Embracer Group', 'Nintendo', 'Nexon',
            'NetEase Games', 'Epic Games', 'Activision Blizzard', 'Riot Games'
        ]
        
        self.countries = [
            'United States', 'France', 'Japan', 'Sweden', 'South Korea', 
            'China', 'Canada', 'United Kingdom', 'Germany', 'Netherlands'
        ]

    def generate_salary_data(self, num_records=200):
        """Génère des données de salaires gaming vs tech"""
        data = []
        
        for _ in range(num_records):
            role = random.choice(self.game_roles)
            experience = random.choice(['Junior', 'Mid', 'Senior'])
            region = random.choice(['North America', 'Europe', 'Asia-Pacific'])
            
            # Base salaires par expérience
            base_salaries = {
                'Junior': {'gaming': 65000, 'tech': 75000},
                'Mid': {'gaming': 95000, 'tech': 110000},
                'Senior': {'gaming': 135000, 'tech': 155000}
            }
            
            # Variation par région
            region_multipliers = {
                'North America': 1.2,
                'Europe': 0.85,
                'Asia-Pacific': 0.75
            }
            
            # Variation par rôle
            role_multipliers = {
                'Game Developer': 1.1, 'Game Designer': 0.95, 'Technical Artist': 1.0,
                'Game Producer': 1.15, 'QA Tester': 0.7, 'Audio Engineer': 0.9,
                'UI/UX Designer': 1.05, 'Game Animator': 0.95, 'Level Designer': 0.9
            }
            
            base_gaming = base_salaries[experience]['gaming']
            base_tech = base_salaries[experience]['tech']
            
            gaming_salary = int(base_gaming * region_multipliers[region] * 
                              role_multipliers[role] * random.uniform(0.85, 1.15))
            tech_salary = int(base_tech * region_multipliers[region] * 
                            role_multipliers[role] * random.uniform(0.9, 1.1))
            
            data.append({
                'role': role,
                'experience_level': experience,
                'gaming_salary_usd': gaming_salary,
                'tech_salary_usd': tech_salary,
                'region': region
            })
        
        return pd.DataFrame(data)

    def generate_studio_data(self):
        """Génère des données de studios gaming"""
        studios_data = []
        
        base_studios = [
            {'name': 'Microsoft Gaming', 'country': 'United States', 'employees': 20100},
            {'name': 'Ubisoft', 'country': 'France', 'employees': 19011},
            {'name': 'Electronic Arts', 'country': 'United States', 'employees': 13700},
            {'name': 'Sony Interactive', 'country': 'Japan', 'employees': 12700},
            {'name': 'Take-Two Interactive', 'country': 'United States', 'employees': 11580},
            {'name': 'Epic Games', 'country': 'United States', 'employees': 4000},
            {'name': 'Riot Games', 'country': 'United States', 'employees': 3500},
            {'name': 'CD Projekt', 'country': 'Poland', 'employees': 1200}
        ]
        
        for studio in base_studios:
            # Calcul salaire moyen basé sur pays et taille
            country_salary_base = {
                'United States': 120000, 'France': 85000, 'Japan': 90000,
                'Poland': 55000, 'Sweden': 75000, 'China': 65000
            }
            
            base_salary = country_salary_base.get(studio['country'], 80000)
            avg_salary = int(base_salary * random.uniform(0.9, 1.3))
            
            studios_data.append({
                'studio_name': studio['name'],
                'country': studio['country'],
                'employees': studio['employees'],
                'avg_salary_usd': avg_salary,
                'retention_rate': random.randint(70, 95),
                'neurodiversity_programs': random.choice([0, 1])
            })
        
        return pd.DataFrame(studios_data)

    def generate_neurodiversity_data(self):
        """Génère des données de ROI neurodiversité"""
        metrics = [
            'Innovation Score', 'Problem Solving Speed', 'Employee Retention',
            'Team Productivity', 'Bug Detection Rate', 'Creative Solutions',
            'Code Quality', 'Debugging Efficiency', 'Learning Speed',
            'Attention to Detail'
        ]
        
        data = []
        for metric in metrics:
            neurotypical = random.randint(70, 100)
            # Neurodiversité généralement meilleure sauf quelques cas
            if metric in ['Team Productivity', 'Learning Speed']:
                neurodiverse = int(neurotypical * random.uniform(0.85, 0.95))
            else:
                neurodiverse = int(neurotypical * random.uniform(1.1, 1.4))
            
            roi = ((neurodiverse - neurotypical) / neurotypical) * 100
            
            data.append({
                'metric': metric,
                'neurotypical_teams': neurotypical,
                'neurodiverse_teams': neurodiverse,
                'roi_percentage': round(roi, 1)
            })
        
        return pd.DataFrame(data)

    def generate_all_data(self):
        """Génère tous les datasets et les sauvegarde"""
        print("🎮 Génération des données Gaming Workforce Observatory...")
        
        # Génération des datasets
        salary_data = self.generate_salary_data()
        studio_data = self.generate_studio_data()
        neurodiversity_data = self.generate_neurodiversity_data()
        
        # Sauvegarde CSV
        salary_data.to_csv('gaming_salaries.csv', index=False)
        studio_data.to_csv('global_studios.csv', index=False)
        neurodiversity_data.to_csv('neurodiversity_roi.csv', index=False)
        
        print("✅ Données générées avec succès!")
        print(f"   - {len(salary_data)} entrées salaires")
        print(f"   - {len(studio_data)} studios analysés")
        print(f"   - {len(neurodiversity_data)} métriques neurodiversité")
        
        return {
            'salaries': salary_data,
            'studios': studio_data,
            'neurodiversity': neurodiversity_data
        }

if __name__ == "__main__":
    generator = GamingDataGenerator()
    data = generator.generate_all_data()
    
    # Aperçu des données
    print("\n📊 Aperçu données salaires:")
    print(data['salaries'].head())
    
    print("\n🏢 Aperçu studios:")
    print(data['studios'].head())
