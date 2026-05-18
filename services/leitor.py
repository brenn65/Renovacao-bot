import pandas as pd

def ler_clientes():
    
    df = pd.read_csv("clientes.csv", sep=";")
    
    return df