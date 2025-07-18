## Multi-Tier Modell Dash

```mermaid
sequenceDiagram
autonumber
    
    box Green User, Browser
    participant User-Agent
    end

    box Purple Python & Libs
    participant Pandas
    participant Dash
    participant Plotly
    participant Flask
    end

    box Blue Datenquellen
    participant CSV
    end

    User-Agent->>Flask: Anfrage URI
    Flask->>Dash: URI parsen
    Dash->>Pandas: Daten anfordern
    Pandas ->> CSV: Daten holen
    Pandas ->> Dash: Daten aufbereitet weiterleiten
    Pandas ->> Plotly: Charts/Plots erstellen
    Pandas ->> Flask: Webinhalte anfordern 
    rect rgb(200, 150, 255)
    Flask->>Flask: Webinhalte liefern
    
    end

    Flask->>User-Agent: HTML,CSS, Javascript
   
```
