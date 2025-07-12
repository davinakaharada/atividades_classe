# 15. Crie uma classe Aluno com os atributos privados nome, nota1 e nota2.
# Implemente um método media() que retorna a média das notas,
# e use getters/setters para acessar os atributos.

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def get_nome(self):
        return self.__nome
    
    def get_nota1(self):
        return self.__nota1
    
    def get_nota2(self):
        return self.__nota2

    def set_nome(self, nome):
        self.__nome = nome

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def media(self):
        return f'O aluno {self.__nome} ficou com uma média de {(self.__nota1 + self.__nota2) / 2}'

aluno = Aluno('Nakaharada', 7.5, 9.8)
print(aluno.media())
aluno.set_nome('Shiro')
aluno.set_nota1(8.5)
print(aluno.media())
