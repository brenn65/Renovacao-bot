from services.leitor import ler_clientes
from services.mensagens import gerar_mensagem
from services.logs import salvar_log
from services.database import criar_tabela
from services.database import salvar_cliente
from services.database import cliente_existe
from datetime import datetime

criar_tabela()

hoje = datetime.now()

df = ler_clientes()

for index, row in df.iterrows():
    vencimento = datetime.strptime(
        row["vencimento"],
        "%Y-%m-%d"
    )
    dias_restantes = (vencimento - hoje).days
    
    mensagem = gerar_mensagem(
        row["nome"],
        row["certificado"],
        dias_restantes
    )
    
    print(mensagem)
    
    salvar_log(row["nome"])
    
    existe = cliente_existe(
        row["telefone"],
        row["certificado"]
    )
    
    if existe:
        print(f"O cliente {row['nome']} já existe!")
    else:
        salvar_cliente(
            row["nome"],
            row["telefone"],
            row["certificado"],
            row["vencimento"]
            
        )
        
    