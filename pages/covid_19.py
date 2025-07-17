# Data dictionary class
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DataDictionary as dd

sub_title = "Covid - nach Bundesland"


df = pd.read_csv("data/covid22-23.csv")
start_val= 'Bayern'

opt = [{"label": k,  "value": k} for k in df.Bundesland.unique()]
# Anfangsbelegung
 


fig = px.line(df[df.Bundesland == start_val], x="Datum", y='Betten', color='Bettenart')
 

register_page(__name__)


 
@callback(
    Output(component_id="controls-and-graph-c19", component_property="figure"),
    Input(component_id="controls-and-check-item-c19", component_property="value"),
)
def update_graph(col_chosen):
    print(col_chosen)
    fig = px.line(df[df.Bundesland.isin([col_chosen])], x="Datum", y='Betten', color='Bettenart')
    return fig


layout = html.Div(
    [
        html.H3(sub_title),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": x, "headerName": x} for x in df.columns],
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
                    id="controls-and-check-item-c19",
                    options=opt, #[{"label": dd.land_abbr(x), "value": x} for x in land],
                    value=[start_val],
                    multi=False,
                ),
        dcc.Graph(figure=fig, id="controls-and-graph-c19"),
    ]
)
