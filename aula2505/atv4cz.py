class Contabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        
        else:
            print("Sem saldo suficiente")
        
    def extrato(self):
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)

contab = Contabancaria("Neymar senior", 100.0)
contab.depositar(100.0)
contab.sacar(25)
contab.sacar(50)
contab.extrato()
            


    