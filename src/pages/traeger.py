# Krankenhäuser nach Trägerschaft
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DataDictionary as dd

sub_title = "Krankenhäuser nach Trägerschaft"


df = pd.read_csv("data/träger_1991-2020.csv", sep=";")
cols_tb = df[["jahr", "ins", "öffentlich", "freigemeinnützig", "privat"]]
cols = ["ins", "öffentlich", "freigemeinnützig", "privat"]

opt = [{"label": " " + dd.raw[k] + " (" + k + ") ", "value": k} for k in cols]
# Anfangsbelegung
start_val = ["ins"]
min, max = df["jahr"].min(), df["jahr"].max()

fig = px.line(df, x="jahr", y=start_val)
 

register_page(__name__)


# fig.add_bar(df, x="jahr", y="insg")
@callback(
    Output(component_id="controls-and-graph-traeg", component_property="figure"),
    Input(component_id="controls-and-check-item-traeg", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.line(df, x="jahr", y=col_chosen)
    return fig


layout = html.Div(
    [
        html.H3(sub_title),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=cols_tb.to_dict("records"),
            columnDefs=[{"field": x, "headerName": dd.raw[x]} for x in cols_tb.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        # dcc.Checklist(
        #     options=opt,
        #     id="controls-and-check-item-traeg",
        #     value=start_val,
        #     inline=True,
        # ),
        dcc.Dropdown(
                    id="controls-and-check-item-traeg",
                    options=opt, #[{"label": dd.land_abbr(x), "value": x} for x in land],
                    value=start_val,
                    multi=True,
                ),
        dcc.Graph(figure=fig, id="controls-and-graph-traeg"),
    ]
)
