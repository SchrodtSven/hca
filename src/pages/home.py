import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html


@callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


dash.register_page(__name__, path="/")

layout = html.Div(
    [
        html.H2("Welcome vto HCA"),
        dbc.Button(
            "Info",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody("Homepage content will follow .... ")),
            id="collapse",
            is_open=False,
        ),
    ]
)
