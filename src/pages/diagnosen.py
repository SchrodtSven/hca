# Diagnosen nach ICD und Jahr
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt 
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import dash_ag_grid as dag
import pandas as pd
sel_cols = ["jahr", "ICD-2", "anzahl"]
all = ['statistics_code', 'jahr','2_variable_code',
       'ICD-2', 'anzahl']
df_diag = pd.read_csv("data/Diag_GES025_DE_2014-2023.csv")[sel_cols]
df_diag.sort_values(by=["jahr"], ascending=False, inplace=True)
min, max = df_diag["jahr"].min(), df_diag["jahr"].max()
register_page(__name__)
dashGridOptions = {"pagination": True}

sub_title = "Diagnosen Deutschland insgesamt - ICD-Codes"


@callback(
    Output("output-container-range-slider-diag", "children"),
    Input("year-range-slider", "value"),
)
def update_output(value):
    a = value[0]
    b = value[1]
    if a > b:
        a, b = b,a
    return 'Aktuelle Auswahl: "{} bis {}"'.format(a, b)


layout = html.Div(
    [
        html.H3(sub_title),
        dcc.RangeSlider(
            min,
            max,
            1,
            value=[2014, 2023],
            id="year-range-slider",
            marks={i: "{}".format(i) for i in range(min, max+1)},
        ),
        html.P(f"Min: {min} Max: {max}"),
        html.Div(id="output-container-range-slider-diag"),
        dag.AgGrid(
            rowData=df_diag.to_dict("records"),
            columnDefs= [{"field": x, "headerName": x.capitalize() } for x in df_diag.columns],
            dashGridOptions={'pagination':True},
        ),
    ]
)