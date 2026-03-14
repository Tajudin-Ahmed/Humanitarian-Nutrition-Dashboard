"""
Interactive Dashboard with Plotly Dash
- Multi-tab layout for program KPIs
- Geospatial & trend visualizations
"""

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Load data
# df = pd.read_csv('../data/processed/cleaned_data.csv')

app.layout = html.Div([
    html.H1("Humanitarian Nutrition & Food Security Dashboard"),
    # Add dropdowns, graphs, etc.
])

if __name__ == '__main__':
    app.run_server(debug=True)
