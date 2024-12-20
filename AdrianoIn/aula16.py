import mysql.connector as mysql
import csv
try:
    conexao = mysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'dbpython'
    )
    print('Conexão estabelecida!')
    for i in range(3):
        print(f'{i+1}º novo dado: ')
        nome_novo = input('Qual o novo nome: ')
        email_novo = input('Qual o nome email: ')
        telefone_novo = input('Qual o novo telefone: ')
        cursor = conexao.cursor()
        sql1 = 'INSERT INTO contatos(nome, email, telefone) VALUES (%s, %s, %s)'
        val1 = (nome_novo, email_novo, telefone_novo)
        cursor.execute(sql1,val1)
        conexao.commit()
     
    cursor = conexao.cursor()
    sql = 'SELECT * FROM contatos ORDER BY nome'
    cursor.execute(sql)
    dados = cursor.fetchall()
    if dados:
        with open('dados.csv','w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(dados)
            print('Dados salvos em dados.csv!')
    else:
        print('Não haviam dados')
except mysql.Error as e:
    print('O erro foi: ', e.msg)