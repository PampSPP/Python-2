class Pessoa:
    def __init__(self, cpf, nome, idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        
    def dados(self):
        return f'CPF: {self.cpf}, Nome: {self.nome}, Idade: {self.idade} anos'
        
    def fumante(self, fumante):
        if fumante == 'F':
            return f'Essa pessoa é fumante.'
        return f'Essa pessoa não é fumante'