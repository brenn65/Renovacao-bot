from datetime import datetime

def salvar_log(nome):
    with open("logs.txt", "a", encoding="utf-8") as log:
        log.write(f"{nome} processado em {datetime.now()}\n")