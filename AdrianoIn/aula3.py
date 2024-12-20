# def calcular_media():
#    soma = 0
#    print('Digite três notas para calcular a média')
#    for _ in range(3):
#        numero = float(input('Qual a nota? '))
#        soma += numero
#    return soma / 3
#media = calcular_media()
#print(f' A média é: {media}')
#def calcular_produto():
#    produto = 1
#    n = int(input('Quantas parcelas? '))
#    for i in range(n):
#        parcela = float(input(f'Qual o valor da {i + 1}ª parcela: '))
#        produto *= parcela
#    return produto
#resultado = calcular_produto()
#print(f' O resultado do produto das parcelas foi {resultado} !')

# nota = input('Qual a nota?')
# def calcular_média(*args):
     

# função dir()
# m_lista = [1,2,3,4,5,6]
# print(sum(m_lista))

# print(dir(m_lista))
# help([].__add__)
# print(dir(__builtins__))


# def args + kwargs
# def exibir_itens (*args, **kwargs):
#    print('args primeiro: ', args)
#    print('kwargs depois: ', kwargs)
# exibir_itens(1,2,3,4, nome='nome', idade= 55, cidade= 'São Paulo')

# def função **kwargs
# def dados_pessoais (**kwargs):
#    for chave, valor in kwargs.items():
#        print(f'{chave}: {valor}' )
# dados_pessoais(nome='nome', idade='55', natural='brasil')

#
# def função *args
#
#def soma(*args):
#    parcela = 0
#    for numero in args:
#        parcela += numero
#    return parcela
def media(*args):
    return sum(args) / len(args)
n = int(input('Quantos serão as parcelas a serem somadas'))
valores = []
for i in range(n):
    valor = float(input(f'Informe o valor da {i + 1}ª parcela de {n}: '))
    valores.append(valor)
calcular_media = media(*valores)
print(f'A média foi de {calcular_media}')
        
#print (soma(1, 2, 3, 4, 5, 6))
    