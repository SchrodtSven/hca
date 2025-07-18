import pandas as pd
data = pd.read_csv(r'data/Anzahl Betten Bundesländer.csv',
                   delimiter=';',
                   header=1)

print(data['Anzahl Betten'].sum(), data['Fallzahlen'].sum())