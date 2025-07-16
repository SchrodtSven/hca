# Diagnosen nach ICD und Jahr
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import dash_ag_grid as dag
import pandas as pd

# from dd import DataDictionary as dd



df_bl = pd.read_csv("data/kh_bulä_geschl_wohnort_2023.csv")
all = ['BB',	'BE',	'BW',	'BY',	'HB',	'HE', 'HH', 'MV', 'NI', 'NW', 'RP', 'SH', 'SL', 'SN', 'ST', 'TH']
sel= ['TH']

register_page(__name__)
dashGridOptions = {"pagination": True}
fig = px.bar(df_bl, x="wohnort", y=sel, color="geschlecht")

sub_title = "Krankenhauspatienten: Bundesländer, Jahre, Geschlecht, Wohnort des Patienten"
layout = [
    dcc.Dropdown(
                    id="land",
                    options=[{"label": ctr, "value": ctr} for ctr in all],
                    value=sel,
                    multi=True,
                ),
    dcc.Graph(figure=fig, id="bar_main")
    
]

@callback(
    Output("bar_main", "figure"), 
    Input("land", "value")
    )

def update_graph(land_chosen):
    fig = px.bar(df_bl, x="wohnort", y=land_chosen, color="geschlecht")
    print(land_chosen)
    return fig