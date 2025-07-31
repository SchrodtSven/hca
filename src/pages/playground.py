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
import dash_daq as daq

theme = {
    "dark": True,
    "detail": "#007439",
    "primary": "#00EA64",
    "secondary": "#6E6E6E",
}
register_page(__name__)

layout = html.Div(
    children=[
        daq.LEDDisplay(
            label="The time is now",
            labelPosition="top",
            value="25.7.12:34",  # A number or a string containing only digits (0-9), periods(.), and colons(:)
        ),
        html.H3("Dash playground"),
        html.H5("Power"),
        daq.LEDDisplay(id="our-LED-display", label="Choose", color="red", value=6),
        dcc.Slider(id="our-LED-display-slider", min=0, max=100, step=1, value=5),
        daq.PowerButton(size=100),
        daq.Gauge(
            min=0,
            max=250,
            value=133,
            color=theme["primary"],
            id="darktheme-daq-gauge",
            className="dark-theme-control",
        ),
        dcc.Slider(id="my-gauge-slider-1", min=0, max=250, step=23, value=133, vertical=True),
        html.Br(),
        daq.Gauge(
            color={
                "gradient": True,
                "ranges": {"green": [0, 6], "yellow": [6, 8], "red": [8, 10]},
            },
            value=2,
            label="Default",
            max=10,
            min=0,
        ),
    ]
)


@callback(Output("darktheme-daq-gauge", "value"), Input("my-gauge-slider-1", "value"))
def update_output(value):
    return value


@callback(Output("our-LED-display", "value"), Input("our-LED-display-slider", "value"))
def update_output(value):
    return str(value)
