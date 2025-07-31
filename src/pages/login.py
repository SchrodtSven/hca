# Assisting file administration
# HCA - Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import (
    Dash,
    html,
    dash_table,
    dcc,
    callback,
    Output,
    Input,
    register_page,
    State,
)
import dash_bootstrap_components as dbc
import pandas as pd
import dash_ag_grid as dag
from hca.dd import DataDictionary as dd
from hca.import_assist import Importer
from hca.cfg import Cfg
sub_title = "Login"

if Cfg.debug:
    register_page(__name__)

email_input = html.Div(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="example-email", placeholder="Enter email"),
        dbc.FormText(
            "Are you on email? You simply have to be these days",
            color="secondary",
        ),
    ],
    className="mb-3",
)

password_input = html.Div(
    [
        dbc.Label("Password", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Enter password",
        ),
        dbc.FormText(
            "A password stops mean people taking your stuff", color="secondary"
        ),
    ],
    className="mb-3",
)

form = dbc.Form([email_input, password_input])

layout = html.Div(
    children=[
        html.H1(
            sub_title,
        ),
        form
    ]
)