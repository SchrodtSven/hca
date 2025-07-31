# Template für Dash page
# HCA - Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-15
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash import (
    Dash,
    html,
    dash_table,
    dcc,
    callback,
    State,
    Output,
    Input,
    register_page,
)
import dash_bootstrap_components as dbc
from hca.dd import DataDictionary as dd
from hca.import_assist import Importer
from hca.formx import FormX
from hca.cfg import Cfg
import time

step = 2
imp = Importer()
fh = FormX()
sub_title = "Testing mutliple Inputs defining column names"
if Cfg.debug:
    register_page(__name__)
col_x = (
    "id", "first", "last", "email",
    "tel", "url" 
)
inputx=fh.input_x(col_x)


layout = html.Div(
    children=[html.H3(sub_title)]
        + inputx
        + [html.Button("Save", id="submit-button"),
        html.Div(id="container-output-text", children="Enter a value and press submit")]
        
    
)

