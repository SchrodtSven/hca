# Import assistant classes
# HCA - Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-21
import dash_mantine_components as dmc
import base64
import datetime
import io
from dash import html
import dash_ag_grid as dag
import pandas as pd

class Importer:
    """Class for file imports:
    - csv
    - ...
    """

    bulletSize = 23
    lineWidth = 4

    steps = {
        "stp_1": "Choose - File(s) and configure ",
        "stp_2": "Configure - Row and Colums ",
        "stp_3": "Preview -   ",
        "stp_4": "Save -  ",
    }

    def __init__(self):
        pass

    def gen_tmel(self, active=0):
        """ Generating timeline for mport assistant

        Args:
            active (int, optional): active step -1 (0 based). Defaults to 0.

        Returns:
            dmc.Timeline: time line with time line items
        """
        children = []
        for k in self.steps:
            # print(self.steps[k])
            tit, txt = self.steps[k].split("-")
            children.append(
                dmc.TimelineItem(
                    title=tit,
                    children=[
                        dmc.Text(
                            [
                                txt,
                                dmc.Anchor("fix-notification", href="#", size="sm"),
                            ],
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                ),
            )

        return dmc.Timeline(
            active=active, bulletSize=self.bulletSize, lineWidth=self.lineWidth, children=children
        )

    def parse_contents(self, contents, filename, date):
        content_type, content_string = contents.split(",")

        decoded = base64.b64decode(content_string)

        try:
            if "csv" in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), sep=";")
            elif "xls" in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))

            df.to_csv(f"uploads/{filename}", index=False)
        except Exception as e:
            print(e)
            return html.Div(["There was an error processing this file."])

        return html.Div(
            [
                html.H5(filename),
                html.H6(datetime.datetime.fromtimestamp(date)),
                # dash_table.DataTable(
                #     df.to_dict('records'),
                #     [{'name': i, 'id': i} for i in df.columns]
                # ),
                dag.AgGrid(
                    id="main_grid_uploaded",
                    rowData=df.to_dict("records"),
                    columnDefs=[
                        {"field": x, "headerName": x} for x in df.columns
                    ],  # df.columns],
                    columnSize="responsiveSizeToFit",
                    dashGridOptions={"pagination": True},
                ),
                html.Hr(),  # horizontal line
                # For debugging, display the raw contents provided by the web browser
                html.Div("Raw Content"),
                html.Pre(
                    #decoded[0:200] + "...",
                    '...',
                    style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
                ),
            ]
        )
