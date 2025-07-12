# 9.Classe Agenda
# Permita adicionar, listar e buscar contatos com nome e telefone.

class Agenda:
    def __init__(self):
        self.contatos = {} # Começamos com um dicionário vazio

    def adicionar(self, nome, telefone):
        if nome not in self.contatos:
            self.contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso.")
        else:
            print(f"O contato '{nome}' já existe na agenda.")

    def listar(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            print("\n--- Contatos na Agenda ---")
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")

    def buscar(self, nome):
        if nome in self.contatos:
            print(f"Telefone de '{nome}': {self.contatos[nome]}")
            return self.contatos[nome]
        else:
            print(f"Contato '{nome}' não encontrado na agenda.")
            return None

minha_agenda = Agenda()

minha_agenda.adicionar("Alice", "987654321")
minha_agenda.adicionar("Bob", "123456789")
minha_agenda.adicionar("Alice", "111222333") 

minha_agenda.listar()

minha_agenda.buscar("Bob")
minha_agenda.buscar("Charlie")

