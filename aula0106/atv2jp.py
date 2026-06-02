class Veiculo:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano
    def informacoes(self):
        print(f"Marca: {self.marca}, Ano:{self.ano}")

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, marca, ano,cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

carro = Carro("Honda",2015,2)
moto = Moto("Yamaha",1903,3)

carro.informacoes()
moto.informacoes()

print(f"Portas:{carro.portas}")
print(f"Cilindradas:{moto.cilindradas}")
