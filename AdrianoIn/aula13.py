import mysql.connector as mysql
nome = input('Qual seu nome: ')
email = input('Qual seu email: ')
telefone = input('Qual seu telefone: ')

try:
    print('\nAbrindo a conexão...')
    conexao = mysql.connect(
        host = '127.0.0.1',
        user = 'root',
        database = 'dbpython'
    )
    print('Conexão realizada com sucesso')
    print('Salvando o banco de dados')
    
    cursor = conexao.cursor()
    sql = 'INSERT INTO contatos(nome, email, telefone) VALUES (%s, %s. %s)'
    vals = (nome, email, telefone)
    conexao.commit()
    
    print('Salvo com sucesso!')
    
except mysql.Error as e:
    print('Ocorreu este erro: ', e.msg)