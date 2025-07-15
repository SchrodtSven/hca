# Template für Dash page
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-15

import dash_mantine_components as dmc
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dd import DataDictionary as dd

df = pd.read_csv()
# fig = px
app = Dash()

app.layout = [
    html.H1(children="Grunddaten der Krankenhäuser", className="app-header",),
    html.Hr(),
    dash_table.DataTable(
        data=df.to_dict("records"),
        columns=[{"name": i, "id": i} for i in df.columns],
        page_size=3,
        style_header={"backgroundColor": "rgb(30, 30, 30)", "color": "white"},
        style_data={"backgroundColor": "rgb(50, 50, 50)", "color": "white"},
    ),
    #dcc.Checklist(options=dta, id='controls-and-check-item', value=['bett'], inline=True),
    #dcc.Graph(figure=fig, id="controls-and-graph"),
    
]

@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-check-item", component_property="value"),
)
   


def update_graph(col_chosen):
    print(col_chosen)
    #foo = df[col_chosen]
    fig = px.line(df_s, x="jahr", y=col_chosen)
    return fig


if __name__ == "__main__":
    app.run(debug=False, port=4711)