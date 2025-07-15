# "Baustellendatei zur Datenbereinigung"
# Projekt Health Care Analysis
# AUTHOR Sven Schrodt
# SINCE 2025-07-14 - Allons enfants!
from helper import DataHelper
from helper import Sanitizer
import pandas as pd



# ex = df['time_label', 'time', 'value', 'value_unit', 'value_variable_code', '2_variable_attribute_code']
# #exit()
# df['dt_iso'] = df.apply(lambda x: Sanitizer.germ_iso(x.datum), axis=1)
# del(df['Unnamed: 5'])

# df.to_csv('data/cv19/mo_san_sh.csv', index=False)



sel_keys = [
    "statistics_code",
    "time",
    "1_variable_code",
    "2_variable_code",
    "2_variable_attribute_code",
    "value" 
    
    
]

target = 'data/Diag_GES025_DE_2014-2023.csv'

df = pd.read_csv('data/23131-0001_de_flat 2.csv', sep=";")
#df.sort_values(by=['time',  '2_variable_attribute_code'], inplace=True)
ex = df[sel_keys]
print(ex.head(10))

ex.to_csv(target, index=False)


#print(df['2_variable_code'].unique())
#print(len(df))



#print(df.groupby(['time',  'value_variable_label']).value_counts())
# data/23131-0001_de_2_san.csv