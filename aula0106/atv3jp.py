class Funcionario:
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibir(self):
        print(f"Nome: {self.nome}, Salário: R$: {self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus
    
gerente = Gerente("Billy JR",50000, 25000)

gerente.exibir()

print(f"Bonus: R$: {gerente.bonus:.2f}")
print(f"Salário total: R$:{gerente.salario_total():.2f}")