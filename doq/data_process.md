# Datenquellen

###  https://www-genesis.destatis.de.  (Statistisches Bundesamt)
### https://www.datenportal.bmbf.de.   (Bundesministerium für Forschung, Technologie und Raumfahrt.)
### https://opendata.rvr.ruhr/.        (Regionalverband Ruhr)


# Datenqualität
# Datenbereinigung

## Probleme
- ### Unterschiedlichste Separatoren / Feld-Begrenzungszeichen
    ```python 
    [ ';', ',', ' ', '"', '\t']
    ``` 
- ### Diverse Datumsformate (DE, ISO, indiv.)

- ### Unterschiedlichste "Prologe"

- ### Nicht normalisierte bis chaotische Daten


<img src="assets/problems.png">


## Lösungswege

- ### Manueller Aufwand (S&R in Dateien per IDE/Shell) <i>zu hoch</i> 
- ### <i>Aktuell genutzt</i>: Python-Snippets, die per Variablen konfigurierbar sind
- ### <i>Optimale Lösung:</i> Assistent


