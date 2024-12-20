class Forma:
    def area (self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        super().__init__(2,lado)
        self.lado = lado
        
    def area(self):
        return self.lado ** 2

print(formas.area())
formas = Quadrado(3)
print(formas.area())
'''
class Carro:
    def __init__(self, marca, modelo, ano, combt, km = 0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combt = combt     
    
    def get_dados(self):
        self.marca = str(input('Qual a marca do carro? '))
        self.modelo = str(input('Qual o modelo? '))
        self.ano = int(input('Qual o ano? '))
        self.km = float(input('Qual a quilometragem? '))
        self.combt = str(input('Qual o tipo de combustível? '))

chamar = Carro()
chamar.get_dados()

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    
    def depositar (self, valor):
        self.__saldo += valor
    
    def get_saldo(self):
        return self.__saldo

corrente = ContaBancaria('AIO')
corrente.depositar(400)
print(corrente.get_saldo())

class Carro:
    def __init__ (self, ligado = True):
        self.ligado = ligado
                
    def get_informacoes (self):
        self.marca = str(input('Qual a marca do carro? '))
        self.modelo = str(input('Qual o modelo? '))
        self.ano = int(input('Qual o ano? '))
        self.km_carro = float(input('Qual a km do veículo? '))
            
    def carro_ligado (self):
        perguntar = input('O carro está ligado, Sim ou Não,?').strip().lower()
        if perguntar == 'Sim':
            print('O carro está ligado')
        else:
            print('O carro está desligado!')
while True:
    chamar = Carro ()
    chamar.get_informacoes()
    chamar.carro_ligado()
    continuando = str(input('Quer continuar? (sim ou não)')).strip().lower()
    if  continuando != 'sim':
        break

class ContaBancaria:
    def __init__ (self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar (self, valor):
        self.saldo += valor
        
    def sacar (self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo Insuficiente')

conta = ContaBancaria('Kauan')
conta.depositar(100)
conta.sacar(30)
print(conta.saldo)

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return print(self.lado ** 2)

lado = float(input('Qual o lado? '))
quadrado = Quadrado(lado)
quadrado.area()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e a idade é {self.idade}')

nome = str(input('Qual seu nome? '))
idade = int(input('Qual sua idade? '))
esta_pessoa = Pessoa(nome, idade)
esta_pessoa.apresentar()

nome2 = str(input('Qual seu nome2? '))
idade2 = int(input('Qual sua idade2? '))
setattr(esta_pessoa, 'nome', nome2)
esta_pessoa.apresentar()

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
                
    def acelerar(self, velocidade):
        self.velocidade = velocidade
        if self.velocidade > 0:
            print(f'O carro está {self.velocidade}')
        else:
            print('Está parado.')
    
marca = str(input('Qual a marca do carro? '))
modelo = str(input('Qual o modelo? '))
ano = int(input('Qual o ano? '))
velocidade = float(input('Qual a veolidade? '))

meu_carro = Carro(marca, modelo, ano)
meu_carro.acelerar(velocidade)

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
    def acelerar(self):
        self.velocidade += 10
        print(f' estamos a {self.velocidade} km/h')
        
    def frear(self):
        if self.velocidade > 0:
            print(f'O carro desacelerou para {self.velocidade} km/h')
        else:
            print('carro parado')

meu_carro = Carro('Nissan', 'Sentra', 2024)
meu_carro.acelerar()
meu_carro.frear()

# usando class
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
meu_carro = Carro('BMW','X9',2025)
print(meu_carro())
'''