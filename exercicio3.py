import Pessoa as p

class PessoaJuridica(p.Pessoa):
    def __init__(self, cnpj, nome, idade):
        super().__init__(cnpj, nome, idade)
        
    def dados(self):
        return f'CNPJ: {self.cpf}, Nome: {self.nome}, Idade: {self.idade} anos'

pessoa_juridica = PessoaJuridica('111222333/12', 'Star Wars Viagens', 2)
print(pessoa_juridica.dados())
print(pessoa_juridica.fumante())