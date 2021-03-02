import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Pharma Sector data
df = pd.read_csv("C:/Users/SSS2015046/Desktop/csv docs/more floors.csv")
df.head(50).dropna()
df1 = df[df['Building'].isin(['Orion Mall','Building(Orian Mall)'])]
df2=df1.set_index(['Building', 'Floor', 'Unit', 'Customer', 'NLA', 'Year']).reset_index()
idx = pd.MultiIndex.from_arrays([df2['Building'], df2['Floor'], df2['Unit'], df2['Customer'],df2['NLA'], df2['Year']])
# , df_s3['Unit of Measure']
df3 = df2.set_index(idx).NLA.unstack(fill_value='')
df3.columns.name = None
df4= df3.reset_index()
df4.head(100)
