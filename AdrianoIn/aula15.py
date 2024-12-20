import mysql.connector as mysql

id = input('Qual registro quer acessar? ')
try:
    conexao = mysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'dbpython'
    )
    print('Conexão realizada!')
    
    cursor = conexao.cursor()
    sql = 'SELECT * FROM contatos WHERE id = %s ORDER BY nome '
    val = (id,)
    cursor.execute(sql, val)
    dados = cursor.fetchone()
    print(dados)
except mysql.Error as e:
    print('O erro foi o seguinte: ', e.msg)