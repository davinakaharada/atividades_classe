# 3.Classe Carro
# Crie uma classe com atributos marca, modelo, ano. Adicione um método descricao().

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f'A marca do carro é {self.marca}, o modelo é {self.modelo} e o ano é {self.ano}'
    
carro1 = Carro('Toyota', 'Civic', 2024)
print(carro1.descricao())