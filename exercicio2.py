import Pessoa as p
    
class PessoaFisica(p.Pessoa):
    def __init__(self, cpf, nome, idade):
        super().__init__(cpf, nome, idade)
        
    def eh_maior(self):
        if self.idade >= 18:
            return True
        return False
    
pessoa2 = PessoaFisica('123456789-12', 'Ubirajara', 49)
print(pessoa2.dados())
print(pessoa2.fumante('n'))
print(pessoa2.eh_maior())