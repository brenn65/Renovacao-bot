def gerar_mensagem(nome, certificado, dias_restantes):
        
    mensagem = f"""Olá {nome}!
    
    Seu certificado digital {certificado} vencerá em {dias_restantes} dias.
    
    Entre em contato conosco clicando no botão abaixo para fazermos a renovação. 
    
    A AR Certicor agradeçe a preferência, não responda está mensagem!
    
    """
    
    return mensagem