# Form creation helper
# HCA - Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-24
from dash import html, dcc


class FormX:
    """Dynamically creating form elements
        - Foo
    """
    
    ph_new = 'New value for:'

    def input_x(self, dta: list) -> list:
        """Generate list/group of input elements from dta

        Args:
            dta (list): list of names for input fields

        Raises:
            ValueError: If empty data set given

        Returns:
            list: list of (dcc.Input)
        """
        if len(dta) == 0:
            raise ValueError("Empty data set in dta!")
        ix = []

        for x in dta:
            ix.append(dcc.Input(id="col_" + str(x), type="text", placeholder=f"{self.ph_new} {x}"))
            
        return ix
