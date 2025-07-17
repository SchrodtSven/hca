# KH Grunddaten
# Projekt Health Care Analysis
# AUTHOR Nadja Post, Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DataDictionary as dd



df = pd.read_csv("data/gkv_fus.csv", sep=";").transpose()
print(df)
df.to_csv("data/gkv_fusion_san.csv")
