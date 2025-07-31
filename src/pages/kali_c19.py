# KH Grunddaten
# HCA - Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!

from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from hca.dd import DataDictionary as dd
import plotly.graph_objects as go

# DataFrame
dta = pd.read_csv("data/cv19/kali_isodat.csv")
sub_title = "Entwicklung Covid-19 Kamp-Lintfort"
register_page(__name__)
fig = px.line(dta[::2], x="isodat", y="Infektionen")
layout = html.Div(
    [
        html.H3(sub_title),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=dta.to_dict("records"),
            columnDefs=[
                {"field": x, "headerName": x} for x in dta.columns
            ],  # df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
   
        dcc.Graph(figure=fig, id="controls-and-graph"),
    ]
)
