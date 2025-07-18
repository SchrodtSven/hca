# Template für Unterseiten
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DataDictionary as dd
import seaborn 
sub_title = "Entwicklung der Krankenhaus- und Bettenanzahl"


df = pd.read_csv("data/23111-0001_de_san.csv", sep=";")
start_val = ["anz_kh", "bett_10k", "bett_aus_dschn"]
fig = px.line(df, x="jahr", y=['start_val'])
# Dropdown mit Optionen
opt = [{"label": " " + dd.raw[k] + " (" + k + ") ", "value": k} for k in tmp]
register_page(__name__)

@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-check-item-basix", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.line(df, x="jahr", y=col_chosen)
    return fig


layout = html.Div(
    [
        html.H3(sub_title),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"field": x, "headerName": dd.raw[x]} for x in df.columns
            ],  # df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        dcc.Dropdown(
            id="controls-and-check-item-basix",
            options=opt,
            value=start_val,
            multi=True,
        ),
        dcc.Graph(figure=fig, id="controls-and-graph"),
    ]
)
