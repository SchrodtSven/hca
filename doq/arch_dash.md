```mermaid
---
config:
  theme: 'handdrawn'
---
journey
    title Dash architecture
    section User-Agent(„Browser“)  
        User Dashboard: Own_dashboard
        Dash.js: 3rd-party
        Plotly.js: 3rd-party 
        Flask.js: 3rd-party 

    section Server
        HCA: Own_app
        Dash: 3rd-party 
        Plotly:3rdparty  
        Flask: 3rd-party 

```