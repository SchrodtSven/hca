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

import pandas as pd
import dash_ag_grid as dag
from hca.dd import DataDictionary as dd
from hca.import_assist import Importer
from hca.cfg import Cfg
sub_title = "Admin Files"

register_page(__name__)


layout = html.Div(
    children=[
        html.H1(
            sub_title,
        ),
        dcc.Upload(
            id="upload-data",
            children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            # Allow multiple files to be uploaded
            multiple=True,
        ),
        html.Div(id="output-data-upload"),
    ]
)



@callback(  
    Output("output-data-upload", "children"),
    Input("upload-data", "contents"),
    #Input("sep_csv", "value"),
    State("upload-data", "filename"),
    State("upload-data", "last_modified"),
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    imp = Importer()
    if list_of_contents is not None:
        children = [
            imp.parse_contents(c, n, d)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children
