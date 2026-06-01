class Animal:
    def __init__(self,comer):
        self.comer = comer
class Cachorro(Animal):
    def __init__(self, comer,latir):
        super().__init__(comer)
        self.latir = latir

animal = Animal("Comendo peixe")
dog = Cachorro("Comendo carne","Latindo")

animal.comer
dog.comer
dog.latir

print(f"Animal:{animal.comer}, Cachorro:{dog.comer},{dog.latir}")