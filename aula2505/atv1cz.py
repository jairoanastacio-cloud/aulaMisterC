class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Bola", 10.0)
produto2 = Produto("Caderno", 20.0)

print(produto1.nome)
print(produto1.preco)
print(produto2.nome)
print(produto2.preco)