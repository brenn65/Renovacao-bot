import pandas as pd
from datetime import datetime

hoje = datetime.now()

df = pd.read_csv("clientes.csv", sep=";")

for index, row in df.iterrows():
    vencimento = datetime.strptime(
        row["vencimento"],
        "%Y-%m-%d"
    )
    dias_restantes = (vencimento - hoje).days
    
    mensagem = f"""
    
    Olá {row['nome']}!
    
    Seu certificado digital {row['certificado']} vencerá em {dias_restantes} dias.
    
    Entre em contato conosco clicando no botão abaixo para fazermos a renovação. 
    
    A AR Certicor agradeçe a preferência, não responda está mensagem!
    
    """
    
    print(mensagem)
    
    with open("logs.txt", "a", encoding="utf-8") as log:
        log.write(f"{row['nome']} processado em {datetime.now()}\n")