import csv
import pandas as pd

filename='final2.csv'

df = pd.read_csv(filename, skiprows=0)

import plotly.express as px
fig1 = px.scatter(df, x='Bits', y='Total Wins')
fig1.show()
