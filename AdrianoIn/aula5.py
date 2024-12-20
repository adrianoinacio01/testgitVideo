# chamando funções para retornar soma, média, maior e menor

from aula5_formas import soma, media, maior, menor

parcelas = []

n = int(input('Quantos numeros vc quer processar? '))

for i in range(n):
    parcela = float(input(f'Qual a {i+1}º número? '))
    parcelas.append(parcela)

print(f'A soma é {soma(*parcelas)}')
print(f'A média é {media(*parcelas)}')
print(f'O maior é {maior(*parcelas)}')
print(f'O menor é {menor(*parcelas)}')




'''
# chamando aula5_formas.py
# realizando cálculos
from aula5_formas import area_circulo, area_quadrado

raio = float(input('Digite o raio: '))
lado = float(input('Digite o lado do quadrado: '))

print('Área do círculo: ', area_circulo(raio))
print('Área do Quadrado: ', area_quadrado(lado))
'''