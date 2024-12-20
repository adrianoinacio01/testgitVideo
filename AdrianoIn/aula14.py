import mysql.connector as mysql

try:
    conexao = mysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'dbpython'
        
    )
    print('Conexão estabelecida...')
    cursor = conexao.cursor()
    sql = 'SELECT * FROM contatos ORDER BY nome'
    cursor.execute(sql)
    dados = cursor.fetchall()
    
    for contato in dados:
        print(contato)
        
except mysql.Error as e:
    print('Ocorreu este erro: ', e.msg)
