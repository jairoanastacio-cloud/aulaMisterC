class Pessoa:
    def __init__(self, nome, idade):
        self.set_nome(nome)
        self.set_idade(idade)
    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        if len (nome.strip()) > 0:
            self.__nome = nome
        else:
            print("O nome tem que ter letras")
    def get_idade(self):
        return self.__idade
    def set_idade(self, idade):
        if 0<= idade <= 120:
            self.__idade = idade
        else:
            print("A idade só é valida entre 0 à 120 anos")
    def falar(self):
        print(f"Eu sou o {self.__nome} e tenho {self.__idade} anos.")
pe = Pessoa("Carlinhos",67)
pe.set_idade(67)
pe.falar()
