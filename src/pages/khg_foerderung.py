# KHG-Investitionsfördermittel - Einzelförderung
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt 
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import dash_ag_grid as dag
import pandas as pd
from hca.dd import DataDictionary as dd



df_bl = pd.read_csv('data/kgh_foerder_1994-2021b.csv')

land = ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg',
       'Bremen', 'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern',
       'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland',
       'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen', 'Deutschland']
 
register_page(__name__)
start_v = ['Deutschland']
dashGridOptions = {"pagination": True}
fig = px.line(df_bl, x="jahr", y=start_v)

sub_title = "KHG-Investitionsfördermittel - Einzelförderung, in Mio. Euro"
layout = [
    html.H3(sub_title),
    dcc.Dropdown(
                    id="land",
                    options=[{"label": dd.land_abbr(x), "value": x} for x in land],
                    value=start_v,
                    multi=True,
                ),
    dcc.Graph(figure=fig, id="bar_main")
    
]

@callback(
    Output("bar_main", "figure"), 
    Input("land", "value")
    )

def update_graph(land_chosen):
    fig = px.line(df_bl, x="jahr", y=land_chosen)
    #fig.add_bar(df_bl["jahr"], y=df_bl[land_chosen])
    print(land_chosen)
    return fig