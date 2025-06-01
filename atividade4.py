# 4.Classe Livro
# Crie uma classe com título, autor, ano. Adicione um método que imprima os dados formatados.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def dados_formatados(self):
        return f'O autor do livro é {self.autor}, o titulo do livro é {self.titulo} e o ano de publicação é {self.ano}'

livro1 = Livro('A raposa', 'Davi', 2017)
print(livro1.dados_formatados())