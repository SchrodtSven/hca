# Analyse Covid-19
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DataDictionary as dd

sub_title = "Covid - nach Bundesland"
register_page(__name__)

df = pd.read_csv("data/covid22-23.csv", parse_dates=True)
# print(df.tail())
# print(df.Bundesland.unique())
# exit()

start_val = ["DE-Summe"]
#print(df[df.Bundesland.isin(start_val)])
opt = [{"label": k, "value": k} for k in df.Bundesland.unique()]
ndf = df[df.Bundesland.isin(start_val)].iloc[::5]
fig = px.line(
    ndf, x="Datum", y="Betten", color="Bettenart", 
)


@callback(
    Output(component_id="controls-and-graph-c19", component_property="figure"),
    Input(component_id="controls-and-check-item-c19", component_property="value"),
)
def update_graph(col_chosen):
    ndf = df[df.Bundesland.isin(col_chosen)]#.iloc[::5]
    
    return px.line(
        data_frame=ndf,
        x="Datum",
        y="Betten",
        color="Bettenart",
    )

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
        dcc.Dropdown(
            id="controls-and-check-item-c19",
            options=opt,  # [{"label": dd.land_abbr(x), "value": x} for x in land],
            value=start_val,
            multi=True,
        ),
        dcc.Graph(figure=fig, id="controls-and-graph-c19"),
    ]
)
