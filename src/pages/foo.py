# Template für Dash page
# HCA - Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-15
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc
from hca.dd import DataDictionary as dd
from hca.import_assist import Importer
step = 2
imp = Importer()
register_page(__name__)
layout = dmc.MantineProvider(
    children=[
        html.H1('Testing timeline for import assistant'),
        imp.gen_tmel(step)
    ]
)
