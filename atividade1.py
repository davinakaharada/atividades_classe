# Classe Retângulo
# 1.Crie uma classe que represente um retângulo com largura e altura. Adicione métodos para calcular a área e o perímetro.

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def area(self):
        area = self.largura * self.altura
        return f'a área do retnângulo é de {area} cm'
    
    def perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        return f'O perímetro do retângulo é de {perimetro} cm'

area = Retangulo(5,12)
print(area.area())
print(area.perimetro())