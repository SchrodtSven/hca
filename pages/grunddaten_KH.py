# Data dictionary class
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt 
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DataDictionary as dd

sub_title = "Entwicklung der Krankenhaus- und Bettenanzahl"



cols = ["anz_kh", "bett_10k", "pat_10k"]
cols_tb = ["anz_kh", "bett_100k", "pat_100k", "jahr"]
df = pd.read_csv("data/23111-0001_de_san.csv", sep=";")[cols_tb]
df['bett_10k']=df['bett_100k'] /10
df['pat_10k']= df['pat_100k'] / 10
opt = [{"label": " " + dd.raw[k] + " (" + k + ") ", "value": k} for k in cols]
# Anfangsbelegung
start_val = ["anz_kh"]

fig = px.line(df, x="jahr", y=start_val)

register_page(__name__)


# fig.add_bar(df, x='jahr', y='insg')
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
            columnDefs= [{"field": x, "headerName": dd.raw[x]} for x in cols], #df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={'pagination':True},
        ),
        # dash_table.DataTable(
        #     data=df.to_dict("records"),
        #     columns=[{"name":dd.raw[i], "id": i} for i in df.columns],
        #     page_size=5
        # ),
        # dcc.Checklist(
        #     options=opt, id="controls-and-check-item-basix", value=start_val, inline=True
        # ),
         dcc.Dropdown(
                    id="controls-and-check-item-basix",
                    options=opt,
                    value=start_val,
                    multi=True,
                ),
        dcc.Graph(figure=fig, id="controls-and-graph")
    ]
)
