import mysql.connector as mysql

nome = input('Informe o nome: ')
email = input('Informe o email: ')
telefone = input('Informe o telefone: ')

try:
    print('\nAbrindo a conexão com o banco de dados...')
    conexao = mysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'dbpython'
    )
    print('Conexão realizada com sucesso')
    print('Salvando no banco de dados...')
    cursor = conexao.cursor()
    sql = 'INSERT INTO contatos(nome,email, telefone) VALUES (%s,%s,%s)'
    vals = (nome, email, telefone)
    cursor.execute(sql,vals)
    conexao.commit()
    print('Salvo com sucesso!')
except mysql.Error as e:
    print('Ocorreu um erro: ', e.msg)