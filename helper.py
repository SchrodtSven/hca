# Data dictionary class
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!

class Helper:
    def flip_dct(dct:dict):
        """ Flipping key <-> value of a Dictionary

        Args:
            dct (dict): _description_

        Returns:
            _type_: _description_
        """
       return  {v: k for k, v in dct.items()}



a = "st;insg;hau_a;na_p,na_p_pfleg"
b = "stichtag;Personal;Hauptamtliche Ärzte;Nichtärztliches Personal;Nichtärztliches Personal im Pflegedienst"


al = a.split(";")
bl = b.split(";")

dct = dict(zip(al, bl))

# print(dct)


dct = {
    "BW": "Baden-Württemberg",
    "BY": "Bayern",
    "BE": "Berlin",
    "BB": "Brandenburg",
    "HB": "Bremen",
    "HH": "Hamburg",
    "HE": "Hessen",
    "MV": "Mecklenburg-Vorpommern",
    "NI": "Niedersachsen",
    "NW": "Nordrhein-Westfalen",
    "RP": "Rheinland-Pfalz",
    "SL": "Saarland",
    "SN": "Sachsen",
    "ST": "Sachsen-Anhalt",
    "SH": "Schleswig-Holstein",
    "TH": "Thüringen",
}

import collections



od = collections.OrderedDict(sorted(dct.items()))

#print(od)


from dd import DataDictionary as dd

#land_flp = {v: k for k, v in DataDictionary.land.items()}

print (dd.land_abbr('Baden-Württemberg'))
