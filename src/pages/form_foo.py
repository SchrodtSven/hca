from dash import (
    Dash,
    html,
    dcc,
    Input,
    Output,
    State,
    MATCH,
    ALL,
    ctx,
    callback,
    register_page,
)
import dash_bootstrap_components as dbc
import dash
from hca.cfg import Cfg

if Cfg.debug:
    register_page(__name__)

dropdown_menu_items = [
    dbc.DropdownMenuItem("Deep thought", id="dropdown-menu-item-1"),
    dbc.DropdownMenuItem("Hal", id="dropdown-menu-item-2"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Clear", id="dropdown-menu-item-clear"),
]

# TODO: check this renders properly once DropdownMenu is updated
input_group = dbc.InputGroup(
    [
        dbc.DropdownMenu(dropdown_menu_items, label="Generate"),
        dbc.Input(id="input-group-dropdown-input", placeholder="name"),
    ]
)


layout = html.Div(
    [
        html.H3("Form Foo"),
        input_group,
    ]
)
style_todo = {"display": "inline", "margin": "10px"}
style_done = {"textDecoration": "line-through", "color": "#888"}
style_done.update(style_todo)


@callback(
    Output("input-group-dropdown-input", "value"),
    [
        Input("dropdown-menu-item-1", "n_clicks"),
        Input("dropdown-menu-item-2", "n_clicks"),
        Input("dropdown-menu-item-clear", "n_clicks"),
    ],
)
def on_button_click(n1, n2, n_clear):
    ctx = dash.callback_context

    if not ctx.triggered:
        return ""
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "dropdown-menu-item-clear":
        return ""
    elif button_id == "dropdown-menu-item-1":
        names = ["Arthur Dent", "Ford Prefect", "Trillian Astra"]
        which = n1 % len(names)
        return names[which]
    else:
        names = ["David Bowman", "Frank Poole", "Dr. Heywood Floyd"]
        which = n2 % len(names)
        return names[which]
