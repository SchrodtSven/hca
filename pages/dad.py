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
from cfg import Cfg
if Cfg.debug:
    register_page(__name__)

image_path = 'assets/dash_b.png'
mt = 'assets/mtier_rere_small.png'
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
            'Dash-Architektur',
           # style={'textAlign': 'center', 'color': '#FFFFFF'}
        ),
          html.Img(src=b64_image(image_path)),
          html.H4('Dateien aus Dash'),
        html.Div(
            html.Pre("""
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
JavaScript                      55          28469          28747         149326
Python                         467          28902          52884          54483
JSON                            65              0              0           1147
Text                            14             19              0             97
HTML                             1              1              0             12
XML                              1              0              0              1
-------------------------------------------------------------------------------
SUM:                           603          57391          81631         205066
-------------------------------------------------------------------------------

++ 

CSV                             65              2              0          97263
                     """)
        ),
        html.H4('Eigene Dateien'),
        html.Div(
            html.Pre("""
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                          32            328            294           1093
JSON                             1              0              0            692
Jupyter Notebook                 6              0           2078            529
Text                             7              4              0            141
CSS                              1              2              0             16
Markdown                         1              0              0              2
-------------------------------------------------------------------------------
SUM:                           48            336             372           2473
-------------------------------------------------------------------------------


                     """)
        ),
        html.H4('Sequenzdiagramm'),
        html.Img(src=b64_image(mt)),
     
    ]
)
