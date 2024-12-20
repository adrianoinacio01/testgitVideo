def pedir_numero():
    i = 0
    while True:
        try:
            num_int = int(input('Informe um número: '))
            print('Número Válido!')
            return num_int
        except ValueError:
            print('Informe número inteiro!')
        finally:
            i += 1
            print(f'Processo realizado pela {i}ª vez')

numero = pedir_numero()
print(f'O número informado é {numero}')

#while pedir_numero() == False

'''
# utilizando try, excepy, e finally
try:
    a = float(input('Informe um número: '))
    b = float(input('Informe outro número: '))
    print(f'A divisão será {a/b:.4f}')
except ZeroDivisionError:
    print('Não dividir por Zero')
except ValueError:
    print('Apenas numeros')
finally:
    print('processo concluso')


# erros e exceções

try:
    numero = int(input('Digite um número: '))
    print(f'Este número ao quadrado é {numero ** 2:.2f}')
except ValueError:
    print('Por Favor somente números inteiros')
'''