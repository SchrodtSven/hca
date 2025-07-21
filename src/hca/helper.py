# Data dictionary class
# HCA - Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!


class Sanitizer:
    """Sanitizing our data

    Returns:
        _type_: _description_
    """

    @staticmethod
    def germ_iso(dte: str):
        """Converting german date (dd.mm.yyyy) to iso (yyyy-mm-dd)

        Returns:
        string: date in ISO 8601 format
        """
        d, m, y = dte.split(".")
        return f"{y}-{m}-{d}"


class DataHelper:
    """Transforming data
    - Transposition
    - Flipping
    - tbd ...
    """

    @staticmethod
    def flip_dct(dct: dict)-> dict:
        """Flipping key <-> value of a Dictionary

        Args:
            dct (dict): _description_

        Returns:
            dict: _description_
        """
        return {v: k for k, v in dct.items()}

    def csv_head_dct(h: str, d: str, sep=";") -> dict:
        al = h.split(sep)
        bl = d.split(sep)
        return dict(zip(al, bl))

    def csv_head_lst(h: str, sep=";") -> list:
        al = h.split(sep)
        return list(al)


class TableHelper:
    def tab_23131():
        sel_keys = [
            "statistics_code",
            "time",
            "1_variable_code",
            "2_variable_attribute_code",
            "value",
            "value_unit",
            "value_variable_code",
            "value_variable_label",
        ]


all_keys = [
    "statistics_code",
    "time_code",
    "time_label",
    "time",
    "1_variable_code",
    "1_variable_label",
    "1_variable_attribute_code",
    "1_variable_attribute_label",
    "2_variable_code",
    "2_variable_label",
    "2_variable_attribute_code",
    "2_variable_attribute_label",
    "value",
    "value_unit",
    "value_variable_code",
    "value_variable_label",
    "value_q",
]
