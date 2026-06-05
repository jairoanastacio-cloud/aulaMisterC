class Funcionario:
    def __init__(self,nome):
        self.nome = nome
    def calcularsalario(self):
        return 0
    
class Vendedor(Funcionario):
    def __init__(self, nome, salariofixo, comissao):
        super().__init__(nome)
        self.salariofixo = salariofixo
        self.comissao = comissao

    def calcularsalario(self):
        return self.salariofixo + self.comissao
    
class Gerente(Funcionario):
    def __init__(self, nome, salariofixo, bonus):
        super().__init__(nome)
        self.salariofixo = salariofixo
        self.bonus = bonus

    def calcularsalario(self):
        return self.salariofixo + self.bonus
    
funcionarios = [
    Vendedor("Megaman", salariofixo=2500, comissao=400),
    Gerente("Freddy", salariofixo=6000, bonus=1400)
]

for func in funcionarios:
    print(f"Funcionario: {func.nome}, Salario total: R$ {func.calcularsalario():.2f}")
