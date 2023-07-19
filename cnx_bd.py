import mysql.connector

def conectar():
    host = 'localhost'
    usuario = 'root'
    senha = 'admin'
    banco_de_dados = 'bancoteste'
    
    conexao = mysql.connector.connect(
        host = host,
        user = usuario,
        password = senha,
        database = banco_de_dados
    )    
    
    return conexao

def criar_tabela(conexao):
    
    cursor = conexao.cursor()
    
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS aluno(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            data_nascimento DATE,
            cidade_natal VARCHAR(255),
            bairro VARCHAR(255)
        )
    ''')
                        
                        
    conexao.commit()
def cadastra_aluno(conexao, nome, data_nascimento, cidade_natal, bairro):  
    cursor = conexao.cursor()
    
    INSERIR_QUERY = '''
    INSERT INTO aluno(nome, data_nascimento, cidade_natal, bairro)
    VALUES(%s, %s, %s, %s)
    
    
    '''  
    
    valores = (nome, data_nascimento, cidade_natal, bairro)
    cursor.execute(INSERIR_QUERY, valores)
    conexao.commit()
    
def main():
    conexao = conectar()
    criar_tabela(conexao)
    
    print('---- CADASTRAR ALUNOS - SENAC ----')
    nome = input('Nome do aluno: ')
    data_nascimento = input('data_nascimento(AAAA-MM-DD):')
    cidade_natal = input('Cidade Natal: ')
    bairro = input('Bairro: ')
    
    cadastra_aluno(conexao, nome, data_nascimento, cidade_natal, bairro)
    
    print('Aluno cadastrado com sucesso!')
    
    conexao.close()
if __name__== '__main__':
    main()
    
    