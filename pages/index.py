# Data dictionary class
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
 

register_page(__name__)

df = px.data.tips()
fig = px.line(df, x='tip', color='time')
 
foo = [1,2,3 ]
layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in foo],
            value=foo[0],
            clearable=False,
        ),
        dcc.Graph(id="bar-chart", figure=fig),
    ]
)