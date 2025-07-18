# Analyse des Gesundheitswesens mit Python &amp; Dash

## Prolog

Prosa folgt

## Shortcuts
- [Installation / Setup](doq/setup_install.md)
- [Schichtenkommunikation - Seqenzdiagramm](doq/dad2.md)
# Ausblick / To-Do


## ASAP 

- Codestruktur optimieren:
    - Strikte Trennung von Text-Content, Layout und Charts/Plots
    - Adminoberfläche mit Verwaltung von Templates für neue Seiten


## Importassistent (div. Quellen: SQL, CSV, XML, APIs)
- Auswahl der Datenquellen
    - Definition der Regeln für Spalten/Zeilen:
        - Fehlende Daten
        - Formate

- Dynamische Diagramme
    - Diagrammtyp und
    - Datenquellen wählbar/kombinerbar

- Implementierung einer HTTP(s) REST-API:
    - JSON
    - XML
    - CSV

- Beyond CSV:
    -  Weitere Persistenzmöglichkeiten: Rel. DBMS, XML, ... 


# Appendix

## Dateistruktur mit Erläuterungen
```
├── app.py (Start und Bootstrapping der App)
├── assets (Verzeichnis für Bilder, Styles etx.)
├── data (Datenhauptverzeichnis)
│   ├── cv19 (Datenverzeichnis)
│   └── dkgev (Datenverzeichnis) 
├── dd.py (Data Dictionary der Daten als Klasse)
├── doq (Dokumentationen als Markdown)
├── file_dd.py (Data Dictionary der Dateinamen/Titel als Klasse)
├── helper.py (Helper-Klassen)
├── pages (Verzeichnis für die Inhalte der Unterseiten)
├── README.md
├── req.txt (Liste der Bibliotheken)
└── tpl.py (Vorlage/template für Unterseiten)
```


## LOC (lines of code)

```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
CSV                             65              2              0          97263
Python                          35            357            367           1160
JSON                             1              0              0            692
Jupyter Notebook                 6              0           2090            529
Text                             8              4              0            155
Markdown                         6             73              0            123
CSS                              1              2              0             16
-------------------------------------------------------------------------------
SUM:                           122            438           2457          99938
-------------------------------------------------------------------------------
```