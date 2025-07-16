# "Baustellendatei zur Datenbereinigung"
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from helper import DataHelper
from helper import Sanitizer
import pandas as pd
from dd import DataDictionary as dd
from helper import DataHelper



f = ['ins', 'öffentlich', 'a_teil', 'freigemeinnützig', 'f_teil',
       'privat', 'pr_teil']

d = {k: k.capitalize() for k in f} 



print(d)
exit()
def to_int(x):
    return x.replace('.', '')

#target = 'data/kh_bulä_geschl_wohnort_2023.csv'
#source = 'data/23131-0012_de_san.csv'
src = 'data/kh_basic_1991-2020.csv'
src='träger_1991-2020.csv'
df = pd.read_csv(src, sep=';')
print(df.head())
