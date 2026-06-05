class Instrumento:
    def __init__(self, nome):
        self.nome = nome
    def tocar(self):
        return 0
    
class Violao(Instrumento):
    def __init__(self, nome):
        super().__init__(nome)
    def tocar(self):
        return "Som de Violão"
    
class Bateria(Instrumento):
    def __init__(self, nome):
        super().__init__(nome)
    def tocar(self):
        return "Som de Bateria"

class Piano(Instrumento):
    def __init__(self, nome):
        super().__init__(nome)
    def tocar(self):
        return "Som de Piano"
    
instrumentos = [
    Violao("Violão"),
    Bateria("Bateria"),
    Piano("Piano")
]

for instrumento in instrumentos:
    print(f"O som do {instrumento.nome} é {instrumento.tocar()}")