import pandas as pd
# 'data/kgh_foerder_1994-2021b.csv'

# '2_variable_code'
# statistics_code,jahr,1_variable_code,2_variable_code,ICD-2,anzahl
src = 'data/Diag_GES025_DE_2014-2023.csv'
df = pd.read_csv(src)
print(df['2_variable_code'].unique())