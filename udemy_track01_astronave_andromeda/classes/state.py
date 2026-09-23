# Desing pattern state
from abc import ABC, abstractmethod


class StatoModulo(ABC):
    @abstractmethod
    def handle_request(self, context):
        pass


class StatoAnalisi(StatoModulo):
    def handle_request(self, context):
        print(f"{context.name} è in stato di analisi dei dati")

class StatoRaccoltaDati(StatoModulo):
    def handle_request(self, context):
        print(f"{context.name} è in stato di raccolta dei dati")

class StatoStandBy(StatoModulo):
    def handle_request(self, context):
        print(f"{context.name} è in stato di standby")       

class StatoManutenzione(StatoModulo):
    def handle_request(self, context):
        print(f"{context.name} è in manutenzione")


class ModuloScientifico():
    def __init__(self, nome):
        self.nome = nome
        self.stato = StatoStandBy()

    def set_state(self, stato):
        self.stato = stato

    def richiesta(self):
        self.stato.handle_request(self)
if __name__ == "__main__":
    pass