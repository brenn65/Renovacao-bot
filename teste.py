import pandas as pd

df = pd.read_csv("clientes.csv", sep=";")

print(df.columns)