# Humanitarian Nutrition Dashboard

<h1 align="center">Humanitarian Nutrition & Food Security Dashboard</h1>

<p align="center">
<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
<img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
<img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white"/>
<img src="https://img.shields.io/badge/SQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub-Portfolio-000000?style=for-the-badge&logo=github&logoColor=white"/>
</p>

---

## **Project Overview**

This repository demonstrates **end-to-end data analysis and visualization of humanitarian nutrition and food security programs**, designed for **WFP / UN data analyst roles**.  

The project includes:

- Nutrition and food security data cleaning and exploration
- Interactive visualizations and dashboards
- Geospatial mapping of vulnerable areas
- Predictive analytics for early warning and program planning
- Automated reporting pipelines for operational decision-making

**Objective:** Enable program managers to **identify malnutrition hotspots, track program coverage, and make data-driven decisions**.

---

## **Project Workflow**

1. **Data Collection & Simulation**
   - Sources: Public datasets, simulated field data
   - Formats: CSV, Excel, JSON

2. **Data Cleaning & Processing**
   - Handle missing values, duplicates, outliers
   - Merge datasets into usable formats

3. **Exploratory Data Analysis (EDA)**
   - Analyze trends in malnutrition, household food security
   - Identify anomalies and key indicators

4. **Geospatial Analysis**
   - Map affected woredas/kebeles
   - Visualize program coverage and gaps

5. **Dashboard & Visualization**
   - Interactive dashboards with **Power BI / Streamlit / Plotly Dash**
   - KPIs: GAM/SAM rates, distribution coverage, stock levels

6. **Predictive Modeling**
   - Forecast malnutrition risk or coverage gaps
   - Scenario analysis (drought, conflict, seasonal variation)

7. **Automated Reporting**
   - Generate weekly or monthly program monitoring reports
   - Automated charts and data summaries

---

## **Repository Structure**

Repository scaffold for a humanitarian nutrition analytics project.

## Project structure

```text
Humanitarian-Nutrition-Dashboard/
│
├── data/
│   ├── raw/                 # Original datasets (nutrition, food security, etc.)
│   ├── processed/           # Cleaned and merged datasets
│   └── sample_data.csv      # Example sample for public use
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_visualization.ipynb
│   ├── 03_geospatial_analysis.ipynb
│   └── 04_predictive_model.ipynb
│
├── dashboards/
│   ├── dashboard_powerbi.pbix
│   ├── dashboard_streamlit.py
│   └── dashboard_plotly_dash.py
│
├── scripts/
│   ├── automate_reporting.py
│   └── data_update_pipeline.py
│
├── figures/                 # Exported charts, graphs, and maps
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## **Installation & Setup**

```bash
# Clone repository
git clone https://github.com/Tajudin-Ahmed/Humanitarian-Nutrition-Dashboard.git
cd Humanitarian-Nutrition-Dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
