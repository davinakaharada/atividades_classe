# 6.Classe Produto
# Crie uma classe com nome, preço e quantidade_estoque. Adicione métodos para vender, repor e aplicar desconto.

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
    
    def vender(self, quantidade):
        self.quantidade_estoque -= quantidade
        return f"Foram vendidas {quantidade} unidades de {self.nome} Estoque atual: {self.quantidade_estoque}"
    
    def repor(self, quantidade):
        self.quantidade_estoque += quantidade
        return f"Foram repostas {quantidade} unidades de {self.nome} Estoque atual: {self.quantidade_estoque}"
    
    def aplicar_desconto(self, percentual):
        valor_desconto = self.preco * (percentual / 100)
        self.preco -= valor_desconto
        return f"Desconto de {percentual}% aplicado em {self.nome} Novo preço: R${self.preco:.2f}"

p = Produto('arroz', 50.00, 100)

print(p.vender(23))
print(p.repor(12))
