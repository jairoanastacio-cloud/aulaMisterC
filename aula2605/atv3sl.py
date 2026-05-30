class ContaB:
    def __init__(self, titular, ):
        self.__titular = titular
        self.__saldo = 0.0
    def depositar(self, valor):
        if valor > 0:
            self.__saldo +=valor
        else:
            print("O valor depositado deve ser maior que 0")
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Sem saldo o suficiente")
    def get_saldo(self):
        return self.__saldo
    def extrato(self):
        print(f"Titular: {self.__titular}, Saldo: {self.__saldo}")

cb = ContaB("Bruce Wayne")
cb.depositar(10000000.00)
cb.sacar(50000.00)
cb.extrato()
