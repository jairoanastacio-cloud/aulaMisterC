class Produto:
    def __init__(self, nome, preco):
        self.set_nome(nome)
        self.set_preco(preco)
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        if len(nome.strip()) > 0:
           self.__nome = nome
        else:
            print("Erro:O produto deve ter letras")
    def get_preco(self):
        return self.__preco
    def set_preco(self,preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro:O preço não pode ser negativo")
produto = Produto("Jaqueta", 80,00)
print(produto.get_nome(),produto.get_preco())
produto.set_preco(90,00)