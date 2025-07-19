# Bettenauslastung nach Bundesländern
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt 
# SINCE 2025-07-15
import pandas as pd
import dash
import plotly.express as px
import plotly.graph_objects as go
import dash_ag_grid as dag
import dash_mantine_components as dmc
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc
from hca.dd import DataDictionary as dd


data = pd.read_csv(r'data/Anzahl Betten Bundesländer.csv',
                   delimiter=';',
                   header=1)

# Erstellen eines DataFrames
df_betten_fallz = pd.DataFrame(data)


register_page(__name__)

# Überprüfen der notwendigen Spalten
required_columns = ['Bundesland', 'Anzahl Betten', 'Fallzahlen']
for col in required_columns:
    if col not in df_betten_fallz.columns:
        raise ValueError(f"Die Spalte '{col}' existiert nicht im DataFrame")

# Verhältnis berechnen
df_betten_fallz['Fälle pro Bett'] = df_betten_fallz['Fallzahlen'] / df_betten_fallz['Anzahl Betten']

# Bundesländer für Dropdown vorbereiten
bundeslaender = [{'label': bl, 'value': bl} for bl in df_betten_fallz['Bundesland'].unique()]
start_val = ['Deutschland-Σ']
layout = [
    html.H1(children="Bettenauslastung nach Bundesländern", className="app-header",),
    html.Hr(),
    
    # Dropdown für Bundesländer
    dcc.Dropdown(
        id='bundesland-dropdown',
        options=bundeslaender,
        value=start_val,    
        multi=True,
        placeholder="Bundesland auswählen...",
        style={'margin-bottom': '20px'}
    ),
    dag.AgGrid(
            id="datatable",
            rowData=df_betten_fallz[df_betten_fallz['Bundesland'].isin([start_val])].to_dict("records"),
            columnDefs=[
                # "headerName": dd.raw[x]}
                {"field": x, "headerName": x}
                for x in df_betten_fallz.columns
            ],  # df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
    
    # dash_table.DataTable(
    #     id='datatable',
    #     data=df_betten_fallz.to_dict("records"),
    #     columns=[{"name": i, "id": i} for i in df_betten_fallz.columns],
    #     page_size=16,
    # ),
    
    dcc.Graph(
        id='combined-chart'
    ),
]

# Callback für die Filterung der Daten basierend auf Dropdown-Auswahl
@callback(
    [Output('datatable', 'rowData'),
     Output('combined-chart', 'figure')],
    [Input('bundesland-dropdown', 'value')]
)
def update_output(selected_bundeslaender):
    # Daten filtern
    filtered_df = df_betten_fallz[df_betten_fallz['Bundesland'].isin(selected_bundeslaender)]
    
    # Tabelle aktualisieren
    table_data = filtered_df.to_dict("records")
    
    # Diagramm aktualisieren
    fig = {
        'data': [
            # Balken für Bettenanzahl (linke Y-Achse)
            go.Bar(
                x=filtered_df['Bundesland'],
                y=filtered_df['Anzahl Betten'],
                name='Bettenanzahl',
                marker=dict(color='lightblue')
            ),
            
            # Linie für Verhältnis (rechte Y-Achse)
            go.Scatter(
                x=filtered_df['Bundesland'],
                y=filtered_df['Fälle pro Bett'],
                name='Fälle pro Bett',
                mode='lines+markers',
                yaxis='y2',
                line=dict(color='red', width=2),
                marker=dict(size=8)
            )
        ],
        'layout': go.Layout(    
            title='Bettenkapazität und Auslastung nach Bundesland',
            yaxis=dict(
                title='Anzahl Betten',
                side='left',
                range=[0, df_betten_fallz['Anzahl Betten'].max() * 1.1]
            ),
            yaxis2=dict(
                title='Fälle pro Bett',
                side='right',
                overlaying='y',
                showgrid=False,
                range=[0, df_betten_fallz['Fälle pro Bett'].max() * 1.1]
            ),
            xaxis=dict(
                title='Bundesland',
                tickangle=-45
            ),
            legend=dict(
                x=1.1,
                y=1
            ),
            margin=dict(l=50, r=50, b=100, t=50, pad=4)
        )
    }
    
    return table_data, fig