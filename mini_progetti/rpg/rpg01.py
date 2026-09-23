from abc import ABC, abstractmethod

class Pg(ABC):
    __slots__ = ["nome", "hp", "atkP", "defP"]
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def atk(self):
        pass647651
        


class Warrior(Pg):
    __slots__ = ["nome", "hp", "atkP", "defP"]

    def __str__(self):
        return f"Un potente guerriero di nome " + self.nome
    def __reprt__():
        pass
    def atk(self):
        return f"{self.nome} sferza un potente colpo di spada!"
    

class Mage(Pg):
    __slots__ = ["nome", "hp", "atkP", "defP"]
    def __str__(self):
        return f"Un potente stregone di nome " + self.nome
    def __reprt__():
        pass
    def atk (self):
        return f"{self.nome} usa un potente incantesimo!"

class Healer(Pg):
    __slots__ = ["nome", "hp", "atkP", "defP"]

    def __str__(self):
        return f"Un potente chieric* di nome " + self.nome
    def __reprt__():
        pass
    def atk(self, nomePg):
        return f"{self.nome} cura {nomePg} di X hp! "

class Thief(Pg):
    __slots__ = ["nome", "hp", "atkP", "defP"]

    def __str__(self):
        return f"Uno scaltro ladro di nome " + self.nome + "con attacco " + self.atkP
    def __reprt__():
        pass
    def atk(self):
        return f"{self.nome} attacca furtivamente con un pugnale! "
    


if __name__ == "__main__":
    aragon = Warrior("Aragon", "50", 170, 230)
    gandalf = Mage("Gandalf")
    bilbo = Thief("Bilbo")
    agatha = Healer("Agatha")
    print(aragon)
    print("\n")
    print(gandalf)
    print("\n")
    print(bilbo)
    print("\n")
    print(agatha)
    print("\n")
    print(aragon.atk())
    print(gandalf.atk())
    print(bilbo.atk())
    print(agatha.atk("bilbo"))
