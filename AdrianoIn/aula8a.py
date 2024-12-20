from dataclasses import dataclass

@dataclass

class Person:
    nome: str
    cpf_cnpj: str
    def tamanho_cpf_cnpj(self): 
        return len(self.cpf_cnpj)
    def __str__(self):
        return f'''Nome: {self.nome} 
                cpf_cnpj: {self.cpf_cnpj}
                comprimento: {self.tamanho_cpf_cnpj()}'''

#def tipo_pessoa(self):
#    if len(self.cpf_cnpj) == 14

if __name__ == '__main__':
    joao = Person(
        'João', '045.098.987-98'
        )
    pedro = Person(
        'Pedro', '987.345.887-23'
        )
    cinam = Person(
        'Centro de Integração Amazonas', '09.987.887/0001-54'
        )
    spet = Person(
        'Empresa de Special Tecnicas', '94.887.098/0001-32'
    )
    print(joao)