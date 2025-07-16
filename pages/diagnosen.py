# Diagnosen nach ICD und Jahr
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import dash_ag_grid as dag
import pandas as pd
sel_cols = ["jahr", "2_variable_attribute_code", "anzahl"]

df_diag = pd.read_csv("data/Diag_GES025_DE_2014-2023.csv")
df_diag.sort_values(by=["jahr"], ascending=False, inplace=True)
min, max = df_diag["jahr"].min(), df_diag["jahr"].max()
register_page(__name__)
dashGridOptions = {"pagination": True}

sub_title = "Diagnosen Deutschland insgesamt"


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
            value=[2023, 2022],
            id="year-range-slider",
            marks={i: "{}".format(i) for i in range(min, max+1)},
        ),
        html.P(f"git sttMIN: {min} max: {max}"),
        html.Div(id="output-container-range-slider-diag"),
        dag.AgGrid(
            rowData=df_diag.to_dict("records"),
            columnDefs= [{"field": x, "headerName": x.capitalize() } for x in df_diag.columns],
            dashGridOptions={'pagination':True},
        ),
    ]
)