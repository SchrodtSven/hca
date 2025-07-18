# Klasse als Data Dictionary für die Zuordnung:
#   - Tabelle - Bedeutung - rel. Dateior
#   - pages{FILENAME} -> Texin Navi
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
class FileDD:

    # Diagnosen DE ins.
    de_icdn = "data/23131-0001_de_2_san.csv"

    codes = {
        "GES025": "Entlassene Patienten",
    }

    pages = {
        "  main  ": "Startseite",
        "Fall bula": "Fallzahlen nach Bundesl.",
        "Admin": "Admin",
        "Diagnosen": "ICD-Code",
        "Downloads": "Downloads",
        "Entw vollkr": "Entwicklung der Vollkräfte ",
        "Grunddaten kh": "KH-Grunddaten",
        "Kh bula": "KH - Bundesländer",
        "Khg foerderung": "KHG-Förderungen",
        "Traeger": "Krankenhäuser nach Trägerschaft",
        "Covid 19": "Covid-19",
        "Basix": "KH-Grunddaten (1991 - 2023)",
        "Gkv hist": "Entwicklung GKV (1994 -2023)",
        "Kh pat": "Patienten vs. Krankenhäuser",
        "Dad": "Dash-Architektur",
        "Quelle dta": "Quellen + Datenmanagement",
        "Z ausblick": "Ausblick"
        
    }
# cloc --by-file --fullpath --match-d 'dash'