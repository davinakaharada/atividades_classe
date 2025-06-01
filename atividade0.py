# 0. Classe Pessoa
# Crie uma classe com os atributos nome e idade. Adicione um método que imprime uma apresentação.

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentacao(self):
        return f'O nome do aluno é {self.nome} e a idade dele é {self.idade} anos'
pessoa1 = pessoa('Davi', 23)
print(pessoa1.apresentacao())