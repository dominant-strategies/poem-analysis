import csv
import pandas as pd

filename='winner.csv'

df = pd.read_csv(filename, skiprows=0)

import plotly.express as px

fig1 = px.scatter(df, x='Bits', y='Winner')
fig1.show()
