meses = ['janeiro', 'fevereiro','março', 'abril','maio', 'junho','julho','agosto','setembro','outubro', 'novembro','dezembro']
print('Me informe uma data!')
dia = int(input('Qual o dia? '))
mes = int(input('Qual o mês (numérico)? '))
ano = int(input('Qual o ano? '))
print(f' A data é Dia {dia} do {meses[mes - 1].upper()} de {ano}')


'''
produto = input('Qual é o tipo de Produto? ')
quantidade = int(input('Qual a quantidade do Produto? '))
preco = float(input('Qual o preço Unitário? '))
total = quantidade * preco
print(f' Produto: {produto}')
print(f' Quantidade: {quantidade}')
print(f' Preço Unitário: R$ {preco:.2f}')
print(f' Total: R$ {total:.3f}')  


for i in range(4):
    if i == 1:
        produto = input('Qual é o tipo de Produto? ')
    elif i == 2:
        quantidade = int(input('Qual a quantidade do Produto? '))
    elif i == 3:
        preco = float(input('Qual o preço Unitário? '))
    elif i == 4:
        total = quantidade * preco
print(f' Produto: {produto}')
print(f' Quantidade: {quantidade}')
print(f' Preço Unitário: R$ {preco:.2f}')
print(f' Total: R$ {total:.3f}')        



# formatando os números
from math import pi
print(f' {pi}')
print(f' {pi:.4f}')
print(f' %.5f '%pi)

texto = 'testando Agora a função in '
print(texto.split())
#print('ago' in texto.lower())

# criando strings
texto = ' O teste é verdadeiro quando é falso'
print(f' 1 {texto.strip()}')
print(f' 2 {texto.upper()}')
print(f' 3 {texto.lower()}')
print(f' 4 {texto.center(10)}')
print(f' 5 {texto.join(['o','join','faz','isso'])}')
print(f' 6 {texto.replace('verdadeiro','verdade')}')
'''