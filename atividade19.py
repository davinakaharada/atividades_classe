# 19. Crie a classe base Veiculo com atributos marca e modelo, e um método exibir_info().
# Crie duas classes filhas Carro e Moto que herdam de Veiculo.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f'A marca do veículo é {self.marca} e o modelo é {self.modelo}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
    
    def exibir_info(self):
        info = super().exibir_info()
        return f'{info} e possui {self.portas} portas'

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_info(self):
        info = super().exibir_info()
        return f'{info} e tem {self.cilindradas} cilindradas'

carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Honda", "CB500", 500)

print(carro1.exibir_info())
print(moto1.exibir_info())