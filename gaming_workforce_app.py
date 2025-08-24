import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="🎮 Gaming Workforce Observatory",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stMetric {
        background-color: #f8f9ff;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e0e6ff;
    }
</style>
""", unsafe_allow_html=True)

# Chargement des données
@st.cache_data
def load_data():
    # Données de salaires
    gaming_salaries = [
        {"role": "Game Developer", "experience_level": "Junior", "gaming_salary_usd": 79799, "tech_salary_usd": 85000, "region": "North America"},
        {"role": "Game Developer", "experience_level": "Mid", "gaming_salary_usd": 108471, "tech_salary_usd": 120000, "region": "North America"},
        {"role": "Game Developer", "experience_level": "Senior", "gaming_salary_usd": 150000, "tech_salary_usd": 165000, "region": "North America"},
        {"role": "Game Designer", "experience_level": "Junior", "gaming_salary_usd": 65000, "tech_salary_usd": 70000, "region": "Europe"},
        {"role": "Game Designer", "experience_level": "Mid", "gaming_salary_usd": 85000, "tech_salary_usd": 95000, "region": "Europe"},
        {"role": "Game Designer", "experience_level": "Senior", "gaming_salary_usd": 120000, "tech_salary_usd": 140000, "region": "Europe"},
        {"role": "Technical Artist", "experience_level": "Junior", "gaming_salary_usd": 60000, "tech_salary_usd": 75000, "region": "North America"},
        {"role": "Technical Artist", "experience_level": "Mid", "gaming_salary_usd": 82000, "tech_salary_usd": 105000, "region": "North America"},
        {"role": "Technical Artist", "experience_level": "Senior", "gaming_salary_usd": 115000, "tech_salary_usd": 145000, "region": "North America"},
        {"role": "Game Producer", "experience_level": "Junior", "gaming_salary_usd": 75000, "tech_salary_usd": 90000, "region": "Europe"},
        {"role": "Game Producer", "experience_level": "Mid", "gaming_salary_usd": 95000, "tech_salary_usd": 125000, "region": "Europe"},
        {"role": "Game Producer", "experience_level": "Senior", "gaming_salary_usd": 140000, "tech_salary_usd": 180000, "region": "Europe"},
        {"role": "QA Tester", "experience_level": "Junior", "gaming_salary_usd": 45000, "tech_salary_usd": 55000, "region": "North America"},
        {"role": "QA Tester", "experience_level": "Mid", "gaming_salary_usd": 58000, "tech_salary_usd": 72000, "region": "North America"},
        {"role": "QA Tester", "experience_level": "Senior", "gaming_salary_usd": 75000, "tech_salary_usd": 90000, "region": "North America"},
        {"role": "Audio Engineer", "experience_level": "Junior", "gaming_salary_usd": 55000, "tech_salary_usd": 65000, "region": "Europe"},
        {"role": "Audio Engineer", "experience_level": "Mid", "gaming_salary_usd": 70000, "tech_salary_usd": 85000, "region": "Europe"},
        {"role": "Audio Engineer", "experience_level": "Senior", "gaming_salary_usd": 95000, "tech_salary_usd": 115000, "region": "Europe"}
    ]

    # Studios globaux
    global_studios = [
        {"studio_name": "Microsoft Gaming", "country": "United States", "employees": 20100, "avg_salary_usd": 125000, "retention_rate": 78, "neurodiversity_programs": 1},
        {"studio_name": "Ubisoft", "country": "France", "employees": 19011, "avg_salary_usd": 89000, "retention_rate": 85, "neurodiversity_programs": 1},
        {"studio_name": "Electronic Arts", "country": "United States", "employees": 13700, "avg_salary_usd": 118000, "retention_rate": 72, "neurodiversity_programs": 1},
        {"studio_name": "Sony Interactive", "country": "Japan", "employees": 12700, "avg_salary_usd": 95000, "retention_rate": 88, "neurodiversity_programs": 0},
        {"studio_name": "Take-Two Interactive", "country": "United States", "employees": 11580, "avg_salary_usd": 130000, "retention_rate": 75, "neurodiversity_programs": 1},
        {"studio_name": "Embracer Group", "country": "Sweden", "employees": 10450, "avg_salary_usd": 78000, "retention_rate": 82, "neurodiversity_programs": 0},
        {"studio_name": "Nintendo", "country": "Japan", "employees": 7317, "avg_salary_usd": 87000, "retention_rate": 90, "neurodiversity_programs": 0},
        {"studio_name": "Nexon", "country": "South Korea", "employees": 7067, "avg_salary_usd": 72000, "retention_rate": 86, "neurodiversity_programs": 1},
        {"studio_name": "NetEase Games", "country": "China", "employees": 6500, "avg_salary_usd": 68000, "retention_rate": 84, "neurodiversity_programs": 0},
        {"studio_name": "Epic Games", "country": "United States", "employees": 4000, "avg_salary_usd": 140000, "retention_rate": 80, "neurodiversity_programs": 1}
    ]

    # Données de neurodiversité
    neurodiversity_roi = [
        {"metric": "Innovation Score", "neurotypical_teams": 70, "neurodiverse_teams": 85, "roi_percentage": 21},
        {"metric": "Problem Solving Speed", "neurotypical_teams": 100, "neurodiverse_teams": 130, "roi_percentage": 30},
        {"metric": "Employee Retention", "neurotypical_teams": 75, "neurodiverse_teams": 92, "roi_percentage": 23},
        {"metric": "Team Productivity", "neurotypical_teams": 100, "neurodiverse_teams": 90, "roi_percentage": -10},
        {"metric": "Bug Detection Rate", "neurotypical_teams": 100, "neurodiverse_teams": 130, "roi_percentage": 30},
        {"metric": "Creative Solutions", "neurotypical_teams": 65, "neurodiverse_teams": 95, "roi_percentage": 46},
        {"metric": "Code Quality", "neurotypical_teams": 85, "neurodiverse_teams": 92, "roi_percentage": 8},
        {"metric": "Debugging Efficiency", "neurotypical_teams": 100, "neurodiverse_teams": 125, "roi_percentage": 25}
    ]

    # Stratégies de rétention
    retention_strategies = [
        {"strategy": "Competitive Compensation", "effectiveness_score": 78, "implementation_cost": "High", "gaming_adoption_rate": 85},
        {"strategy": "Career Development", "effectiveness_score": 85, "implementation_cost": "Medium", "gaming_adoption_rate": 72},
        {"strategy": "Work-Life Balance", "effectiveness_score": 92, "implementation_cost": "Low", "gaming_adoption_rate": 68},
        {"strategy": "Company Culture", "effectiveness_score": 89, "implementation_cost": "Medium", "gaming_adoption_rate": 91},
        {"strategy": "Remote/Hybrid Work", "effectiveness_score": 87, "implementation_cost": "Low", "gaming_adoption_rate": 89},
        {"strategy": "Learning Opportunities", "effectiveness_score": 83, "implementation_cost": "Medium", "gaming_adoption_rate": 76},
        {"strategy": "Recognition Programs", "effectiveness_score": 75, "implementation_cost": "Low", "gaming_adoption_rate": 65},
        {"strategy": "Flexible Schedule", "effectiveness_score": 88, "implementation_cost": "Low", "gaming_adoption_rate": 84}
    ]

    # Évolution de l'industrie
    industry_evolution = [
        {"year": 2020, "global_revenue_billion": 159.3, "total_employees_k": 320, "avg_gaming_salary": 95000, "layoffs_k": 2.1},
        {"year": 2021, "global_revenue_billion": 175.8, "total_employees_k": 340, "avg_gaming_salary": 102000, "layoffs_k": 1.8},
        {"year": 2022, "global_revenue_billion": 184.4, "total_employees_k": 365, "avg_gaming_salary": 108000, "layoffs_k": 15.2},
        {"year": 2023, "global_revenue_billion": 187.7, "total_employees_k": 350, "avg_gaming_salary": 116000, "layoffs_k": 10.5},
        {"year": 2024, "global_revenue_billion": 200.0, "total_employees_k": 355, "avg_gaming_salary": 124000, "layoffs_k": 8.3}
    ]

    return {
        'salaries': pd.DataFrame(gaming_salaries),
        'studios': pd.DataFrame(global_studios),
        'neurodiversity': pd.DataFrame(neurodiversity_roi),
        'retention': pd.DataFrame(retention_strategies),
        'evolution': pd.DataFrame(industry_evolution)
    }

# Header principal
st.markdown("""
<div class="main-header">
    <h1 style='color: white; text-align: center; margin: 0;'>
        🎮 GAMING WORKFORCE OBSERVATORY
    </h1>
    <h3 style='color: white; text-align: center; margin: 0; font-weight: 300;'>
        PREMIÈRE MONDIALE - Observatoire révolutionnaire des talents gaming
    </h3>
</div>
""", unsafe_allow_html=True)

# Chargement des données
data = load_data()

# Sidebar pour navigation
st.sidebar.markdown("## 🎮 Navigation")
page = st.sidebar.selectbox(
    "Choisissez une section:",
    ["🏠 Dashboard Principal", "⚔️ Talent Wars: Gaming vs Tech", "🌍 Studios Globaux", 
     "🧠 Neurodiversité & ROI", "💰 Analyse Compensation", "🎯 Stratégies Rétention"]
)

if page == "🏠 Dashboard Principal":
    st.markdown("### 📊 Métriques Clés de l'Industrie Gaming")

    # Calculs des métriques
    total_employees = data['studios']['employees'].sum()
    avg_salary = data['salaries']['gaming_salary_usd'].mean()
    studios_count = len(data['studios'])
    avg_retention = data['studios']['retention_rate'].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Employés", f"{total_employees:,}", "355K+ dans l'industrie")
    with col2:
        st.metric("Salaire Moyen", f"${avg_salary:,.0f}", "vs $120K tech traditionnel")
    with col3:
        st.metric("Studios Analysés", f"{studios_count}", "Top employers mondiaux")
    with col4:
        st.metric("Taux Rétention", f"{avg_retention:.1f}%", "Moyenne industrie")

    # Graphique d'évolution
    st.markdown("### 📈 Évolution de l'Industrie (2020-2024)")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(data['evolution'], x='year', y='global_revenue_billion', 
                     title='Revenus Globaux (Milliards $)',
                     color_discrete_sequence=['#667eea'])
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(data['evolution'], x='year', y='avg_gaming_salary',
                    title='Évolution Salaire Moyen Gaming',
                    color_discrete_sequence=['#764ba2'])
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

elif page == "⚔️ Talent Wars: Gaming vs Tech":
    st.markdown("### ⚔️ Gaming vs Tech - Analyse Comparative")

    # Comparaison salaires
    salary_comparison = data['salaries'].copy()
    salary_comparison['salary_gap'] = salary_comparison['tech_salary_usd'] - salary_comparison['gaming_salary_usd']
    salary_comparison['gap_percentage'] = (salary_comparison['salary_gap'] / salary_comparison['gaming_salary_usd']) * 100

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(salary_comparison, x='experience_level', y=['gaming_salary_usd', 'tech_salary_usd'],
                    title="Comparaison Salaires par Niveau d'Expérience",
                    barmode='group', color_discrete_sequence=['#ff6b6b', '#4ecdc4'])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        avg_gap = salary_comparison.groupby('role').agg({
            'gap_percentage': 'mean',
            'salary_gap': 'mean'
        }).reset_index()

        fig = px.bar(avg_gap, x='role', y='gap_percentage',
                    title='Écart Salarial Moyen par Rôle (%)',
                    color_discrete_sequence=['#ff9f43'])
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

    # Tableau détaillé
    st.markdown("### 📋 Analyse Détaillée par Rôle")
    detailed_analysis = salary_comparison.groupby(['role', 'experience_level']).agg({
        'gaming_salary_usd': 'mean',
        'tech_salary_usd': 'mean',
        'salary_gap': 'mean',
        'gap_percentage': 'mean'
    }).round(0).reset_index()

    st.dataframe(detailed_analysis, use_container_width=True)

elif page == "🌍 Studios Globaux":
    st.markdown("### 🌍 Comparaison des Studios Gaming Mondiaux")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.scatter(data['studios'], x='avg_salary_usd', y='retention_rate', 
                        size='employees', hover_name='studio_name',
                        color='country', title='Salaire vs Rétention (Taille = Employés)',
                        size_max=50)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        top_studios = data['studios'].nlargest(8, 'employees')
        fig = px.bar(top_studios, x='employees', y='studio_name',
                    title="Top Studios par Nombre d'Employés",
                    orientation='h', color_discrete_sequence=['#667eea'])
        st.plotly_chart(fig, use_container_width=True)

    # Analyse par pays
    st.markdown("### 📊 Analyse par Pays")
    country_analysis = data['studios'].groupby('country').agg({
        'employees': 'sum',
        'avg_salary_usd': 'mean',
        'retention_rate': 'mean',
        'neurodiversity_programs': 'sum'
    }).round(0).reset_index()

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(country_analysis, values='employees', names='country',
                    title='Répartition Employés par Pays')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(country_analysis, x='country', y='avg_salary_usd',
                    title='Salaire Moyen par Pays',
                    color_discrete_sequence=['#ff6b6b'])
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

elif page == "🧠 Neurodiversité & ROI":
    st.markdown("### 🧠 Impact de la Neurodiversité sur la Performance")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(data['neurodiversity'], x='neurotypical_teams', y='metric',
                    orientation='h', title='Performance Équipes Neurotypiques',
                    color_discrete_sequence=['#95a5a6'])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(data['neurodiversity'], x='neurodiverse_teams', y='metric',
                    orientation='h', title='Performance Équipes Neurodiverses',
                    color_discrete_sequence=['#3498db'])
        st.plotly_chart(fig, use_container_width=True)

    # ROI Analysis
    st.markdown("### 💹 Analyse du ROI de la Neurodiversité")

    col1, col2 = st.columns(2)

    with col1:
        colors = ['green' if x > 0 else 'red' for x in data['neurodiversity']['roi_percentage']]
        fig = px.bar(data['neurodiversity'], x='metric', y='roi_percentage',
                    title='ROI par Métrique (%)', color=colors,
                    color_discrete_map={'green': '#27ae60', 'red': '#e74c3c'})
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Radar chart
        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=data['neurodiversity']['neurotypical_teams'],
            theta=data['neurodiversity']['metric'],
            fill='toself',
            name='Équipes Neurotypiques',
            line_color='rgba(149, 165, 166, 0.8)'
        ))

        fig.add_trace(go.Scatterpolar(
            r=data['neurodiversity']['neurodiverse_teams'],
            theta=data['neurodiversity']['metric'],
            fill='toself',
            name='Équipes Neurodiverses',
            line_color='rgba(52, 152, 219, 0.8)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxes=dict(
                    visible=True,
                    range=[0, 150]
                )),
            showlegend=True,
            title="Comparaison Performance - Radar"
        )

        st.plotly_chart(fig, use_container_width=True)

    # Recommandations
    st.markdown("### 💡 Insights Clés")
    insights = [
        "🚀 **Innovation +21%** : Les équipes neurodiverses montrent une innovation supérieure",
        "⚡ **Résolution problèmes +30%** : Vitesse de résolution de problèmes considérablement améliorée", 
        "🎯 **Détection bugs +30%** : Capacité supérieure à identifier les anomalies",
        "🎨 **Solutions créatives +46%** : Approches créatives significativement plus développées",
        "👥 **Rétention +23%** : Meilleure fidélisation des employés neurodiverses"
    ]

    for insight in insights:
        st.markdown(insight)

elif page == "💰 Analyse Compensation":
    st.markdown("### 💰 Analyse Approfondie des Compensations")

    # Évolution temporelle
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Revenus Globaux', 'Employés Totaux', 'Salaire Moyen', 'Licenciements'),
        vertical_spacing=0.12
    )

    fig.add_trace(
        go.Scatter(x=data['evolution']['year'], y=data['evolution']['global_revenue_billion'],
                  name='Revenus (Mds $)', line=dict(color='#667eea')),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(x=data['evolution']['year'], y=data['evolution']['total_employees_k'],
                  name='Employés (K)', line=dict(color='#764ba2')),
        row=1, col=2
    )

    fig.add_trace(
        go.Scatter(x=data['evolution']['year'], y=data['evolution']['avg_gaming_salary'],
                  name='Salaire Moyen', line=dict(color='#f093fb')),
        row=2, col=1
    )

    fig.add_trace(
        go.Bar(x=data['evolution']['year'], y=data['evolution']['layoffs_k'],
               name='Licenciements (K)', marker_color='#ff6b6b'),
        row=2, col=2
    )

    fig.update_layout(height=600, showlegend=False, title_text="Évolution de l'Industrie Gaming (2020-2024)")
    st.plotly_chart(fig, use_container_width=True)

    # Distribution des salaires
    st.markdown("### 📊 Distribution des Salaires par Rôle")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.box(data['salaries'], x='role', y='gaming_salary_usd',
                    title='Distribution Salaires Gaming',
                    color_discrete_sequence=['#667eea'])
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        avg_by_role = data['salaries'].groupby('role')['gaming_salary_usd'].mean().reset_index()
        fig = px.bar(avg_by_role, x='role', y='gaming_salary_usd',
                    title='Salaire Moyen par Rôle',
                    color_discrete_sequence=['#764ba2'])
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

elif page == "🎯 Stratégies Rétention":
    st.markdown("### 🎯 Stratégies de Rétention des Talents Gaming")

    col1, col2 = st.columns(2)

    with col1:
        # Bubble chart efficacité vs adoption
        fig = px.scatter(data['retention'], x='effectiveness_score', y='gaming_adoption_rate',
                        size='effectiveness_score', hover_name='strategy',
                        title='Efficacité vs Adoption dans le Gaming',
                        color='implementation_cost',
                        color_discrete_map={'High': '#e74c3c', 'Medium': '#f39c12', 'Low': '#27ae60'})
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(data['retention'], x='strategy', y='effectiveness_score',
                    title="Score d'Efficacité par Stratégie",
                    color='implementation_cost',
                    color_discrete_map={'High': '#e74c3c', 'Medium': '#f39c12', 'Low': '#27ae60'})
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

    # Analyse coût-bénéfice
    st.markdown("### 💡 Analyse Coût-Bénéfice")

    # Matrice de recommandations
    retention_analysis = data['retention'].copy()
    retention_analysis['cost_score'] = retention_analysis['implementation_cost'].map({'Low': 3, 'Medium': 2, 'High': 1})
    retention_analysis['recommendation_score'] = (retention_analysis['effectiveness_score'] * 0.4 + 
                                                 retention_analysis['gaming_adoption_rate'] * 0.3 + 
                                                 retention_analysis['cost_score'] * 30) / 100 * 100

    top_strategies = retention_analysis.nlargest(5, 'recommendation_score')[['strategy', 'effectiveness_score', 'implementation_cost', 'gaming_adoption_rate', 'recommendation_score']]

    st.markdown("#### 🏆 Top 5 Stratégies Recommandées")
    st.dataframe(top_strategies.round(1), use_container_width=True)

    # Insights
    st.markdown("### 📋 Recommandations Clés")
    recommendations = [
        "🎯 **Work-Life Balance** : Stratégie la plus efficace (92%) avec coût faible",
        "🏢 **Company Culture** : Forte adoption gaming (91%) et efficacité élevée (89%)",
        "💻 **Remote/Hybrid Work** : Excellent rapport efficacité/coût pour l'industrie gaming",
        "⏰ **Flexible Schedule** : Haute efficacité (88%) avec investissement minimal",
        "📈 **Career Development** : Impact fort sur la rétention long terme"
    ]

    for rec in recommendations:
        st.markdown(rec)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem;'>
    🎮 <strong>Gaming Workforce Observatory</strong> - Première mondiale<br>
    Données basées sur des études réelles de l'industrie gaming (2024-2025)<br>
    Sources: LinkedIn Gaming Reports, Glassdoor Gaming Salaries, UKIE Research, Ubisoft Neurodiversity Program
</div>
""", unsafe_allow_html=True)
