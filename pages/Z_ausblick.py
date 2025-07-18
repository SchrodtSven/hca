# Template für Dash page
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt 
# SINCE 2025-07-15
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc
from dd import DataDictionary as dd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import geopandas as gpd
import contextily as ctx
import base64

image_path = 'assets/dash_b.png'
mt = 'assets/mtier_rere_small.png'
register_page(__name__)
# Using base64 encoding and decoding
def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
      image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

#calling the above function
html.Img(src=b64_image(image_path))

layout = html.Div(
    #style={'backgroundColor': '#000000', 'color': '#FFFFFF', 'padding': '20px'},
    children=[
        html.H1(
            'Ausblick',
           # style={'textAlign': 'center', 'color': '#FFFFFF'}
        ),
        dcc.Markdown("""
- ### Importassistent (div. Quellen: SQL, CSV, XML, APIs)
    - Auswahl der Datenquellen
    - Definition der Regeln für Spalten/Zeilen:
        - Fehlende Daten
        - Formate

        
- ### Dynamische Diagramme 
    -  #### Diagrammtyp und 
    - #### Datenquellen wählbar/kombinerbar
    
    

- ### Implementierung einer HTTP(s) REST-API:
    - JSON
    - XML
    - CSV
    
    

- ### Beyond DataFrame:
    - Persistenzmöglichkeiten: Rel. DBMS, XML, ... 
                     """)
     
    ]
)
