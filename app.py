# Data dictionary class
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!

# 3rd party libs
from dash import (
    Dash,
    html,
    page_registry,
    page_container,
    clientside_callback,
    Input,
    Output,
    dcc,
)

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash

load_figure_template(["sandstone", "simplex"])

# project libs
from file_dd import FileDD
from cfg import Cfg


# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.FLATLY, dbc_css],
    suppress_callback_exceptions=True,
)
app.title = "Health Care Analysis"
dash.register_page(__name__)
navbar = dbc.NavbarSimple(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(FileDD.pages[page["name"]], href=page["path"])
                for page in page_registry.values()
                if page["module"] != "pages.not_found_404"
            ],
            nav=True,
            label="Auswahl",
        ),
    ],
    brand=Cfg.title,
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container([navbar, page_container], fluid=True, className="dbc")

app.server.route('/')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
