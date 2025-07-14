# Data dictionary class
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
from dd import DataDictionary as dd

sub_title = "Entwicklung der Krankenhaus- und Bettenanzahl"
#tab_cols =  ["jahr","anz_kh", "bett_100k", "pat_100k"]
df = pd.read_csv("data/23111-0001_de_san.csv", sep=";")

print(df.columns)


#["jahr","anz_kh", "bett_100k", "pat_100k"]

# Keys: 'anz_kh', 'bett', 'bett_100k','pat_100k', 'ber_bch', 'verweil_dschn', 'bett_aus_dschn'

cols = ["anz_kh", "bett_100k", "pat_100k"]




#df.columns=[dd.raw[k]  for k in df.keys()]
dta = [{"label": " " + dd.raw[k] + " (" + k + ") ", "value": k} for k in cols]
# Anfangsbelegung
start_val = ["anz_kh"]

fig = px.line(df, x="jahr", y=start_val)

register_page(__name__)


# fig.add_bar(df, x='jahr', y='insg')
@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-check-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.line(df, x="jahr", y=col_chosen)
    return fig


layout = html.Div(
    [
        html.H3(sub_title),
        dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name":dd.raw[i], "id": i} for i in df.columns],
            page_size=5,
            #style_header={"backgroundColor": "rgb(30, 30, 30)", "color": "white"},
            #style_data={"backgroundColor": "rgb(50, 50, 50)", "color": "white"},
        ),
        dcc.Checklist(
            options=dta, id="controls-and-check-item", value=start_val, inline=True
        ),
        dcc.Graph(figure=fig, id="controls-and-graph"),
        # dcc.Graph(id="bar-chart", figure=fig)
    ]
)
