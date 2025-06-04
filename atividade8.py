# 8.Classe Elevador
# A classe deve conter andar_atual, total_andares, capacidade e pessoas. Crie métodos para subir, descer, entrar e sair.

class Elevador:
    def __init__(self, andar_atual, total_andares, capacidade, pessoas):
        self.andar_atual = andar_atual
        self.total_andares = total_andares
        self.capacidade = capacidade
        self.pessoas = pessoas
    
    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            return f'Você subiu mais um andar. Andar Nº {self.andar_atual}'
        else:
            return f'Você já está no ultimo andar'
    
    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            return f'Você desceu um andar. Andar atual Nº {self.andar_atual}'

    def entrar(self):
        if self.pessoas < self.capacidade:
            self.pessoas += 1
        else:
            return f'A capacidade maxima de pessoas foi atingida!!!'
        
    def sair(self, quantidade_pessoas):
        if self.pessoas - quantidade_pessoas >= 0:
            self.pessoas -= quantidade_pessoas
            return f'{quantidade_pessoas} pessoas saíram. Total de pessoas: {self.pessoas}'
        else:
            return f'Não há {quantidade_pessoas} pessoas para sair. Apenas {self.pessoas} pessoas no elevador.'
    
pessoa = Elevador(13, 17,12,7)
