# SMS DA

## Multi-Tier Modell Dash

```mermaid
sequenceDiagram
autonumber
    
    box Green User, Browser
    participant User-Agent
    end

    box Yellow Flask
    participant Webserver
    end

    box Purple Python & Libs
    participant Python
    participant Pandas
    participant Dash
    participant Plotly
    participant Flask
    end

    box Blue Datenquellen
    participant CSV
    end

    User-Agent->>Webserver: Anfrage URI
    Webserver->>Python: URI parsen
    Python->>Pandas: Daten anfordern
    Pandas ->> CSV: Daten holen
    Python ->> Dash: Daten aufbereitet weiterleiten
    Python ->> Plotly: Charts/Plots erstellen
    Python ->> Flask: Webinhalte anfordern 
    rect rgb(200, 150, 255)
    Flask->>Python: Webinhalte liefern
    
    end

    Webserver->>User-Agent: HTML,CSS, Javascript
   
```
