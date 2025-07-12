# 23. Crie uma classe Animal com método falar().
# Crie as subclasses Cachorro e Gato que sobrescrevem esse método com sons específicos.

class Animal:
    def falar(self):
        return "O animal faz um som."

class Cachorro(Animal):
    def falar(self):
        return "Au au"

class Gato(Animal):
    def falar(self):
        return "Miau"

cachorro1 = Cachorro()
gato1 = Gato()

print(cachorro1.falar()) 
print(gato1.falar())      
