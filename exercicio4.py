class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario
    
    def get_salario(self, usuario):
        if usuario == 'autorizado':
            return self.__access_salario()
        return f'Você não tem autorização'
    
    def __access_salario(self):
        return self._salario
    
professor1 = Professor('Joao', 40, 5000)
print(professor1.get_salario('autorizado'))