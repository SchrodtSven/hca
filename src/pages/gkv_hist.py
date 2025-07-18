# Quantitative Entwicklung der GK
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag


sub_title = "Quantitative Entwicklung der GKV"
df_f = pd.read_csv("data/gkv_fusion_san.csv")
fig_2 = fig = px.line(df_f, x="Jahr", y="Anzahl")
df = pd.read_csv("data/gkv_hist_san.csv")

# opt = [{"label": " " + dd.raw[k] + " (" + k + ") ", "value": k} for k in tmp]
# Anfangsbelegung
tmp = list(df.columns)
# Jahr ist obligatorisch (X-Achse)
del tmp[0]


opt = [{"label": k, "value": k} for k in tmp]
start_val = ["AOK", "BKK", "IKK", "Ersatzkassen", "(LKK) SVLFG", "Knappschaft / Sk"]
fig = px.line(df, x="Jahr", y=start_val)

register_page(__name__)

 
@callback(
    Output(component_id="controls-and-graph-gkvh", component_property="figure"),
    Input(component_id="controls-and-check-item-gkvh", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.line(df, x="Jahr", y=col_chosen)
    print(col_chosen)
    return fig


layout = html.Div(
    [
        html.H3(sub_title),
        html.H4("Anzahl der Krankenkassen"),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[
                # "headerName": dd.raw[x]}
                {"field": x, "headerName": x}
                for x in df.columns
            ],  # df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        dcc.Dropdown(
            id="controls-and-check-item-gkvh",
            options=opt,
            value=start_val,
            multi=True,
        ),
        dcc.Graph(figure=fig, id="controls-and-graph-gkvh"),
        html.H4("Fusionsverlauf jeweils zum 1. Januar"),
        dcc.Graph(figure=fig_2, id="controls-and-graph-gkvh-fus"),
    ]
)
