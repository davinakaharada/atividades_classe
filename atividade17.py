# 17. Implemente a classe Produto com atributos privados nome e preco.
# Crie um método aplicar_desconto(percentual) que modifica o preço, mas sem permitir que ele fique abaixo de zero.

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco


    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

 
    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço inválido. Deve ser maior ou igual a zero.")


    def aplicar_desconto(self, percentual):
        if percentual < 0:
            return "Desconto inválido."
        novo_preco = self.__preco - (self.__preco * percentual / 100)
        if novo_preco < 0:
            return "Desconto não pode deixar o preço negativo."
        self.__preco = novo_preco
        return f"Desconto aplicado. Novo preço: R${self.__preco:.2f}"


a = Produto('Camiseta', 110)
print(f"Preço original: R${a.get_preco():.2f}")
print(a.aplicar_desconto(10))  
print(f"Preço final: R${a.get_preco():.2f}")
