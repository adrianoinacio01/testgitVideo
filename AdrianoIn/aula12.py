import mysql.connector as mysql

try:
    conexao = mysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'dbpython'
    )
    print(conexao)
except mysql.Error as e:
    print(e.msg)