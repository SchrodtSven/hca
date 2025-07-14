
# Data dictionary class 
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-11
class DataDictionary:

    
    """_summary_
        Quelle: https://www-genesis.destatis.de
        Tabellen: 23111-0001,  23121-0001,23611 
        Grunddaten der Krankenhäuser
        Deutschland
    """
    raw = {
        "jahr": "Jahr",
        "anz_kh": "Krankenhäuser",
        "bett": "Betten",
        "bett_:100k": "Betten je 100.000 Einwohner",
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
        "priv": "Private Haushalte/Priv.Organisat.oh.Erwerbszweck",
        "sum": "Insgesamt",
        "kosten_ber": "Bereinigte Kosten",
        "kst_kh": "Bereinigte Kosten je Krankenhaus",
        "kst_fall": "Bereinigte Kosten je Behandlungsfall",
    }

    @staticmethod
    def trans(key: str):
        if key in DataDictionary.raw:
            return DataDictionary.raw[key]
        else:
            raise ValueError(f"Non-existent key {key}!")


