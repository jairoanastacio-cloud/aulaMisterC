class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco 

    def desc(self, porcentagem):
        precoatual = self.preco - (self.preco * porcentagem /100)
        return precoatual
    
produto = Produto("teclado", 50.0)

print("Nome:", produto.nome)
print("Preço:", produto.preco)
print("Preço com desconto:", produto.desc(10))