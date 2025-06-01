# 2.Classe Círculo
# Crie uma classe Circulo com atributo raio. Implemente métodos para calcular área e circunferência.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        area = 3.14 * self.raio **2
        return f'A área do circulo é de {area:.2f} cm'
    
    def circunferencia(self):
        circunferencia = 2 * 3.14 * self.raio
        return f'A circunferência do círculo é de {circunferencia:.2f} cm'

valor = Circulo(5)
print(valor.area())
print(valor.circunferencia())