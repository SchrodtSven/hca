# Template für Dash page
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt 
# SINCE 2025-07-15
import pandas as pd
import dash
import plotly.express as px
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dd import DataDictionary as dd

data = pd.read_csv(r'data/Anzahl Betten Bundesländer.csv',
                   delimiter=';',
                   header=1)

# Erstellen eines DataFrames
df_betten_fallz = pd.DataFrame(data)

# Überprüfen der notwendigen Spalten
required_columns = ['Bundesland', 'Anzahl Betten', 'Fallzahlen']
for col in required_columns:
    if col not in df_betten_fallz.columns:
        raise ValueError(f"Die Spalte '{col}' existiert nicht im DataFrame")

# Verhältnis berechnen
df_betten_fallz['Fälle pro Bett'] = df_betten_fallz['Fallzahlen'] / df_betten_fallz['Anzahl Betten']


layout = [
    html.H1(children="Bettenauslastung nach Bundesländern", className="app-header",),
    html.Hr(),
    dash_table.DataTable(
        data=df_betten_fallz.to_dict("records"),
        columns=[{"name": i, "id": i} for i in df_betten_fallz.columns],
        page_size=15,
        style_header={"backgroundColor": "rgb(30, 30, 30)", "color": "white"},
        style_data={"backgroundColor": "rgb(50, 50, 50)", "color": "white"},
    ),
    #dcc.Checklist(options=dta, id='controls-and-check-item', value=['bett'], inline=True),
    #dcc.Graph(figure=fig, id="t_controls-and-graph"),
    
]