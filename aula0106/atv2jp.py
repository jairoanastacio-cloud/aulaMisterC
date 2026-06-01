class Veiculo:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.ports = portas

class Moto(Veiculo):
    def __init__(self, marca, ano,cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

