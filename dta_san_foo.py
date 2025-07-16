# "Baustellendatei zur Datenbereinigung"
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from helper import DataHelper
from helper import Sanitizer
import pandas as pd
from dd import DataDictionary as dd
from helper import DataHelper

target = 'data/kh_bulä_geschl_wohnort_2023.csv'
source = 'data/23131-0012_de_san.csv'
df = pd.read_csv(source, sep=";")
print(df.keys())
df['wo_abbr'] = df['wohnort'].map(dd.land_abbr)


# 2023;Insgesamt;Deutschland;1964736;2698007;788739;491827;172838;469993;1255897;385973;1566454;4209671;843770;241213;868973;499144;542228;523559
# 2023;männlich;unbekannt;-;-;-;-;3;-;3;-;-;-;-;3;-;-;-;
# 2023;weiblich;unbekannt;-;;-;;-;;-;;2;-;;6;-;;-;;-;;-;


#ext = df.groupby('1_variable_code').value_counts()
print(df.head(12))

df.to_csv(target, index=False)



exit()
#df.sort_values(by=['time',  '2_variable_attribute_code'], inplace=True)
ex = df[sel_keys]
print(ex.head(10))

ex.to_csv(target, index=False)


#print(df['2_variable_code'].unique())
#print(len(df))



#print(df.groupby(['time',  'value_variable_label']).value_counts())
# data/23131-0001_de_2_san.csv