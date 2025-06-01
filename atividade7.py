# 7.Classe ContaBancaria
# Crie uma classe com métodos depositar, sacar e extrato.

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, quantidade):
        self.saldo += quantidade
        return f'A quantidade depositada foi de R${quantidade},00 reais'
    
    def sacar(self, quantidade):
        self.saldo -= quantidade
        return f'A quantidade retirada foi de R${quantidade},00 reais'
    
    def extrato(self):
        return f'Seu extrato é de {self.saldo}'

cliente = ContaBancaria(5000)
cliente.depositar(570)
cliente.sacar(1720)
print(cliente.extrato())
