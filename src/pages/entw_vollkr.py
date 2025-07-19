# Entwicklung der Vollkräfte
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt 
# SINCE 2025-07-14 - Allons enfants!
from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from hca.dd import DataDictionary as dd
frm = 2013
to = 2023
sub_title = f"Entwicklung der Vollkräfte  {frm} - {to}" 
df = pd.read_csv('data/23111-0002_de_san.csv', sep=';').query(f"jahr >= {frm} and jahr <= {to}")
 

register_page(__name__)
cols = ['jahr','insg','hau_a','na_p', 'na_p_pfleg'] 
fig = px.bar(df, x='jahr', y=cols, labels={x: dd.raw[x] for x in cols}, barmode="group")
#fig.add_bar(df, x='jahr', y='insg')
options = [{'label': dd.raw[k] + ' ('+k + ')',  'value':k }for k in cols]

layout = html.Div(
    [   
        html.H1(sub_title),
         dag.AgGrid(
            id="datatable",
            rowData=df[cols].to_dict("records"),
            columnDefs=[
                # "headerName": dd.raw[x]}
                {"field": x, "headerName": dd.raw[x] +' ('+x+')' }
                for x in df.columns
            ],  # df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        dcc.Dropdown(
                    id="vollk-drop",
                    options = options,
                    value=cols[1:],
                    multi=True,
                ),
        dcc.Graph(id="bar-chart", figure=fig)
    ]
)