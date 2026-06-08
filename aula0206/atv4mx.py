class Pagamento:
    def processar(self, valor):
        self.valor = valor

class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95

class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02

class Pix(Pagamento):
    def processar(self, valor):
        return valor
    

pagamento = [Dinheiro(), Cartao(), Pix()]

print(f"Valor original do pagamento: R$ {pagamento.processar}\n")

for pagamento in pagamento:
    print("Valor final: R$", pagamento.processar(100))