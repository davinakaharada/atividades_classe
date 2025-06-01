# 5.Classe Aluno com Notas
# Crie uma classe com nome e lista de notas. Implemente métodos para adicionar notas, calcular média e verificar aprovação.

class Aluno_com_notas:
    def __init__(self,nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_notas(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovacao(self, media_minima=5):
        media = self.calcular_media()
        if media >= media_minima:
            return f'{self.nome} foi Aprovado com média {media}'
        else:
            return f'{self.nome} foi Reprovado com média {media}'

aluno1 = Aluno_com_notas('davi')
aluno1.adicionar_notas(9)
aluno1.adicionar_notas(7)
aluno1.adicionar_notas(6)
aluno1.adicionar_notas(8)
aluno1.adicionar_notas(10)
print(aluno1.verificar_aprovacao())