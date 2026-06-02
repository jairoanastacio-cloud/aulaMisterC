class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    def apresentar(self):
        print(f"Aluno: {self.nome}, Idade: {self.idade}, Matricula: {self.matricula}")


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    def apresentar(self):
        print(f"Professor: {self.nome}, Idade: {self.idade}, Salario: {self.salario}")

aluno = Aluno("William", 982, 7)
prof = Professor("Vitor Felipe Kogisteski Magalhães da Silva Santos Programador PHP Junior e Programador CObol Senior e Jogador pela seleção Daiana do Paraná",9980 , 2026)
