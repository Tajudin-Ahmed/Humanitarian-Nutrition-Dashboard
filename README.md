# Humanitarian Nutrition Dashboard

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
