# Data dictionary class
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-11
class DataDictionary:
    """Data Dictionary
    Quellen:
        https://www-genesis.destatis.de
        Tabellen: 23111-*,  23121-*,  23111-*, 23611-*
        https://www.datenportal.bmbf.de
        https://opendata.rvr.ruhr/
    
    Grunddaten der Krankenhäuser
    Deutschland
    """

    raw = {
        "jahr": "Jahr",
        "anz_kh": "Krankenhäuser",
        "bett": "Betten",
        "bett_100k": "Betten je 100.000 Einwohner",
        "pat": "Patienten",
        "pat_100k": "Patienten je 100.000 Einwohner",
        "ber_bch": "Berechnungs-/Belegungstage",
        "verweil_dschn": "Durchschnittliche Verweildauer",
        "bett_aus_dschn": "Durchschnittliche Bettenauslastung",
        "oef_h": "Öffentliche Haushalte",
        "gkv": "Gesetzliche Krankenversicherung",
        "spv": "Soziale Pflegeversicherung",
        "grv": "Gesetzliche Rentenversicherung",
        "guv": "Gesetzliche Unfallversicherung",
        "pkv": "Private Krankenversicherung",
        "ag": "Arbeitgeber",
        "priv": "Private Haushalte o. Organisat. oh. Erwerbszweck",
        "sum": "Insgesamt",
        "kosten_ber": "Bereinigte Kosten",
        "kst_kh": "Bereinigte Kosten je Krankenhaus",
        "kst_fall": "Bereinigte Kosten je Behandlungsfall",
        "st": "stichtag",
        "insg": "Personal",
        "hau_a": "Hauptamtliche Ärzte",
        "na_p": "Nichtärztliches Personal",
        "na_p_pfleg": "Nichtärztliches Personal Pflege",
        "datum": "Datum",
        "infekt_sum": "Gesamtzahl der Infektionen",
        "infekt_ink": "Zuwachs seit der letzten Meldung",
        "genesen": "Genesen",
        "verstorben": "Verstorben",
        "holy_inzidenz": "Inzidenzwert",
    }

    land = {
        "BB": "Brandenburg",
        "BE": "Berlin",
        "BW": "Baden-Württemberg",
        "BY": "Bayern",
        "HB": "Bremen",
        "HE": "Hessen",
        "HH": "Hamburg",
        "MV": "Mecklenburg-Vorpommern",
        "NI": "Niedersachsen",
        "NW": "Nordrhein-Westfalen",
        "RP": "Rheinland-Pfalz",
        "SH": "Schleswig-Holstein",
        "SL": "Saarland",
        "SN": "Sachsen",
        "ST": "Sachsen-Anhalt",
        "TH": "Thüringen",
    }

    land_flp = {v: k for k, v in land.items()}

    @staticmethod
    def trans(key: str) -> str:
        if key in DataDictionary.raw:
            return DataDictionary.raw[key]
        else:
            raise ValueError(f"Non-existent key {key}!")

    def land_lng(key: str) -> str:
        if key in DataDictionary.land:
            return DataDictionary.land[key]
        else:
            raise ValueError(f"Non-existent key {key}!")

    def land_abbr(key: str) -> str:
        if key in DataDictionary.land_flp:
            return DataDictionary.land_flp[key]
        else:
            raise ValueError(f"Non-existent key {key}!")
