# criando operações
import math

def soma (*args):
    return sum(args)

def media(*args):
    if len(args) == 0:
        print('Calculo da média: Divisão por zero!')
        return 0
    return soma(*args) / len(args)

def maior(*args):
    return max(args)

def menor (*args):
    return min(args)




# criando um module math
''' import math

def area_circulo(raio):
    return math.pi * (raio ** 2)

def area_quadrado (lado):
    return lado ** 2
    
'''