class Funcionario:
    def __init__(self, nome, matricula, salariofixo):
        self.__nome = nome
        self.__matricula = matricula
        self.setsalariofixo(salariofixo)

    def nome(self):
        return self.__nome
    
    def matricula(self):
        return self.__matricula
    
    def salariofixo(self):
        return self.__salariofixo
    
    def setsalariofixo(self, valor):
        if valor < 0:
            print("Salário não pode ser negativo")
            self.__salariofixo = 0
        else:
            self.__salariofixo = valor

    def calcularsalario(self):
        return 0
    
    def exibir(self):
        tipo_funcionario = self.__class__.__name__
        print(f"Nome: {self.nome()}, Matricula:{self.matricula()}, Tipo:{tipo_funcionario},Salário Total: R${self.calcularsalario():.2f}")

class Clt(Funcionario):
    def __init__(self, nome, matricula, salariofixo):
        super().__init__(nome, matricula, salariofixo)
    def calcularsalario(self):
        return self.salariofixo() 

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salariofixo, totalvendas):
        super().__init__(nome, matricula, salariofixo)
        self.__totalvendas = totalvendas
    def calcularsalario(self):
        comissao = self.__totalvendas * 0.10
        return self.salariofixo() + comissao 

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salariofixo):
        super().__init__(nome, matricula, salariofixo)
        self.__bonus = 67000.00
    def calcularsalario(self):
        return self.salariofixo() + self.__bonus
    
funcionarios = [
    Clt("Jorge","215",9999.99),
    Vendedor("Diego","967",10000.00, totalvendas=200.00),
    Gerente("Seistovisck Setesson","67",670000.00)
]

for f in funcionarios:
    f.exibir()