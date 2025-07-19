# Quellen + Datenmanagement
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-15
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc
from hca.dd import DataDictionary as dd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import geopandas as gpd
import contextily as ctx
import base64
from hca.cfg import Cfg
if Cfg.debug:
    register_page(__name__)
    
image_path = "assets/problems.png"
 


# Using base64 encoding and decoding
def b64_image(image_filename):
    with open(image_filename, "rb") as f:
        image = f.read()
    return "data:image/png;base64," + base64.b64encode(image).decode("utf-8")


# calling the above function
html.Img(src=b64_image(image_path))

layout = html.Div(
    # style={'backgroundColor': '#000000', 'color': '#FFFFFF', 'padding': '20px'},
    children=[
    #     html.H1(
    #         "Quellen + Datenmanagement",
    #         # style={'textAlign': 'center', 'color': '#FFFFFF'}
    #     ),
    html.Hr(),
        dcc.Markdown(""" 
# Quellen


- ###  https://www-genesis.destatis.de.  
  ###  (Statistisches Bundesamt)
- ### https://www.datenportal.bmbf.de.   
  ###   (Bundesministerium für Forschung, Technologie und Raumfahrt.)
- ### https://opendata.rvr.ruhr/.        
  ### (Regionalverband Ruhr)

#  
# 
# 

---

# Datenbereinigung

## Probleme

- ### Unterschiedlichste Separatoren / Feld-Begrenzungszeichen
    
    ``` [ ';', ',', ' ', '"', '\t'] ```
    
- ### Diverse Datumsformate (DE, ISO, indiv.)

- ### Unterschiedlichste "Prologe"

- ### Nicht normalisierte bis chaotische Daten


## Lösungswege

- ### Manueller Aufwand: (S&R in Dateien per IDE/Shell) zu hoch 
- ### Aktuell genutzt: Python-Snippets, die per Variablen konfigurierbar sind
- ### Optimale Lösung: Assistent
                      """),
        html.Hr(),
        html.Img(src=b64_image(image_path)),
    ]
)
