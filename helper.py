# Data dictionary class
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!

class Sanitizer:
    """ Sammlung von Methoden zur Datenbereinigung

    Returns:
        _type_: _description_
    """
    @staticmethod
    def germ_iso(dte:str):
        pass



class DataHelper:
    """ Sammlung von Methoden zum Umgang mit Daten
        - Transposition
        - Flipping
        - tbd ... 

    Returns:
        _type_: _description_
    """
    @staticmethod
    def flip_dct(dct:dict):
        """ Flipping key <-> value of a Dictionary

        Args:
            dct (dict): _description_

        Returns:
            _type_: _description_
        """
        return  {v: k for k, v in dct.items()}



