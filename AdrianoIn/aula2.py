# exemplo de utilização de listas
#lista1 = [1, 2, 3, 'python', True, 0, 12.4] #lista simples
#lista2 = [[1,'s', 2.2],[2.2, 0, 'cs']]
#print(lista1[3])
#lista1[6] = 1.5
#print(lista1)
#lista1.append('acrescimo')
#print(lista1)
#lista1.remove(1)
#print(lista1)
#print(len(lista1))
#print(2 in lista1)
#print(22 in lista1)
#print(lista1.index('python'))
#print(lista2)
#print(lista2[0][1])
#pilha = [] #criando pilha vazia
#pilha.append(1)
#pilha.append('ss')
#pilha.append(2.2)
#print(pilha)
#print(pilha.pop())
#pilha.extend([22,22,2.3,'iii'])
#print(pilha)
#pilha = pilha + ['1',1]
#print(pilha)
#tupla = (44,44,55)
#print(tupla)
dicio = {
    'num1': 20.0,
    'num2': 12,
    'num3': 125.43254 / 235
    }
#print(dicio['num3'])
#dicio['num3'] = 45 ** 5
#print(dicio['num3'])
#print(dicio.keys())
#print(dicio.values())
#print(dicio.items())
#print('num1' in dicio.keys())
#print(type(dicio['num2']))
employ = {
    'nomes': [],
    'idades': []
    }
nome = str(input(' Qual seu nome? '))
employ['nomes'].append(nome)
idade = int(input(' Qual sua idade? '))
employ['idades'].append(idade)
print(nome,idade, employ)
#notas.append(bime2)
#bime3 = float(input(' Qual foi sua nota no 3º Bimestre: '))
#notas.append(bime3)
#bime4 = float(input(' Qual foi sua nota no 4º Bimestre: '))
#notas.append(bime4)
#print('a maior nota foi: ',max(notas),' a menor: ', min(notas), ' a média foi: ', sum(notas)/len(notas))
#print ('A sua média foi: ', (bime1 + bime2 + bime3 + bime4) / 4)