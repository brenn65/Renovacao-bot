import sqlite3

def conectar():
    
    conn = sqlite3.connect("banco.db")
    
    return conn

def criar_tabela():
    
    conn = conectar()
    cursor = conn.cursor ()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes_processados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome text,
            telefone text,
            certificado text,
            vencimento text,
            enviado_em text
            
        )
        """
    )
    conn.commit()
    
    conn.close()
    
def salvar_cliente(nome, telefone, certificado, vencimento):
        
        conn = conectar()
        
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO clientes_processados
            (nome, telefone, certificado, vencimento)
            
            VALUES
            (?, ?, ?, ?)
            """,
            (nome, telefone, certificado, vencimento)
        )
        conn.commit()
        
        conn.close()
        
def cliente_existe(telefone, certificado):
    
        conn = conectar()
        
        cursor = conn.cursor()  
        
        cursor.execute(
            """
            SELECT *
            FROM clientes_processados
            WHERE telefone = ?
            AND certificado = ?
            """,
            (telefone, certificado)
        )
        
        resultado = cursor.fetchone()
        conn.close()
        return resultado
    