# Entwicklung der Krankenhaus- und Patientenanzahl
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt 
# SINCE 2025-07-15
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc
from hca.dd import DataDictionary as dd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import geopandas as gpd
import contextily as ctx


try:
    df = pd.read_csv(
        r'data/KH Anz., Pat. Anz..csv',
        header=4,
        delimiter=';',
        on_bad_lines='skip'
    )
    # Spaltennamen bereinigen
    df.columns = df.columns.str.strip()
    required_columns = ['Jahr', 'Krankenhäuser\nAnzahl', 'Patienten\nAnzahl']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Fehlende Spalte: {col}")
except Exception as e:
    print(f"Fehler beim Laden der CSV: {e}")
    exit()


register_page(__name__)

layout = html.Div(
    #style={'backgroundColor': '#000000', 'color': '#FFFFFF', 'padding': '20px'},
    children=[
        html.H1(
            'Entwicklung der Krankenhaus- und Patientenanzahl',
           # style={'textAlign': 'center', 'color': '#FFFFFF'}
        ),
        
        html.Div([
            html.Label('Metrik auswählen:', style={'color': '#FFFFFF'}),
            dcc.Checklist(
                id='metric-checklist',
                options=[
                    {'label': 'Anzahl Krankenhäuser', 'value': 'Krankenhäuser'},
                    {'label': 'Anzahl Patienten', 'value': 'Patienten'}
                ],
                value=['Krankenhäuser'],
               # labelStyle={'display': 'block', 'margin-top': '5px'}
            )
        ], style={'padding': '20px'}),

        dcc.Graph(id='time-series-plot'),

        html.Div([
            dcc.RangeSlider(
                id='year-slider',
                min=df['Jahr'].min(),
                max=df['Jahr'].max(),
                value=[df['Jahr'].min(), df['Jahr'].max()],
                marks={str(year): str(year) for year in df['Jahr'].unique()},
                step=None,
                tooltip={'placement': 'bottom'}
            )
        ], style={'padding': '40px'})
    ]
)

# Callback für Interaktivität
@callback(
    Output('time-series-plot', 'figure'),
    [Input('metric-checklist', 'value'),
     Input('year-slider', 'value')]
)
def update_graph(selected_metrics, year_range):
    filtered_df = df[
        (df['Jahr'] >= year_range[0]) & 
        (df['Jahr'] <= year_range[1])
    ].copy()

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Krankenhäuser (linke Y-Achse)
    if 'Krankenhäuser' in selected_metrics:
        fig.add_trace(
            go.Scatter(
                x=filtered_df['Jahr'],
                y=filtered_df['Krankenhäuser\nAnzahl'],
                mode='lines+markers',
                name='Krankenhäuser (Anzahl)',
                line=dict(color='#00FF00', width=2)
            ),
            secondary_y=False
        )

    # Patienten (rechte Y-Achse)
    if 'Patienten' in selected_metrics:
        fig.add_trace(
            go.Scatter(
                x=filtered_df['Jahr'],
                y=filtered_df['Patienten\nAnzahl'],
                mode='lines+markers',
                name='Patienten (Anzahl)',
                line=dict(color='#FFA500', width=2)
            ),
            secondary_y=True
        )

    # Layout anpassen
    fig.update_layout(
        title='Krankenhäuser vs. Patienten',
        # plot_bgcolor='#000000',
        # paper_bgcolor='#000000',
        # font=dict(color='#FFFFFF'),
        # hovermode='x unified',
        legend=dict(orientation='h', yanchor='bottom', y=1.02),
        xaxis=dict(
            showgrid=True,  # X-Achsen-Grid LINIEN ANZEIGEN
          #  gridcolor='#333333'  # Farbe der Gridlinien
        )
    )

    # Y-Achsen (ohne horizontale Gitterlinien)
    fig.update_yaxes(
        title_text='Anzahl Krankenhäuser',
        secondary_y=False,
        showgrid=False  # Horizontale Linien entfernen
    )
    fig.update_yaxes(
        title_text='Anzahl Patienten',
        secondary_y=True,
        showgrid=False  # Horizontale Linien entfernen
    )

    return fig
