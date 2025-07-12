# 21. Crie a classe Funcionario com nome e salário. 
# Crie Gerente e Vendedor como subclasses, adicionando atributos específicos. Exiba as informações usando herança.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
    
    def info(self):
        return f'O gerente do departamento de {self.departamento} tem um salário de {self.salario}'
        
    
class Vendedor(Funcionario):
    def __init__(self, nome, salario, vendas, comissao):
        super().__init__(nome, salario)
        self.vendas = vendas
        self.comissao = comissao

    def info(self):
        return f'O funcionário {self.nome} tem um salário de {self.salario}, fez {self.vendas} vendas neste mês e recebeu uma comissão de {self.comissao}.'

gerente1 = Gerente("Carlos", 8000, "Vendas")
vendedor1 = Vendedor("Ana", 3000, 20, "5%")

print(gerente1.info())
print(vendedor1.info())



