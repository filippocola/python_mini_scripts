from abc import ABC, abstractmethod
# Design pattern composite (tutto - parti )
# esempio directory (composite - contenitori) e files (foglie)

class ComponenteAstronave(ABC):
    def __init__(self, nome):
        self.nome = nome
        @abstractmethod
        def operazione(self):
            pass
        def aggiungi(self, componente):
            pass
        def rimuovi(self, componente):
            pass
        def ottieniFiglio(self, index):
            pass

class Sistema(ComponenteAstronave):
    def operazione(self):
        print(f"Sistema {self.nome} in operazione")


class ModuloComplesso(ComponenteAstronave):
    def __init__(self, nome):
        super().__init__(nome)
        self._componenti = []
    def operazione(self):
        print(f"Modulo Complesso {self.nome} in operazione:")
        for componente in self._componenti:
            componente.operazione()
    def aggiungi(self, componente):
        self._componenti.append(componente)
    def rimovi(self, componente):
        self._componenti.remove(componente)
    def ottieniFiglio(self, index):
        if index < 0 or index >= len(self._componenti):
            return None
        return self._componenti[index]
    

if __name__ == "__main__":
    # Singoli sistemi (foglia)
    sistema_navigazione = Sistema("Navigazione")
    sistema_difesa = Sistema("Difesa")
    sistema_ricerca = Sistema("Ricerca Scientifica")

    # Modulo composito con aggiunta di foglie 
    modulo_composito = ModuloComplesso("Modulo Comando")
    modulo_composito.aggiungi(sistema_navigazione)
    modulo_composito.aggiungi(sistema_difesa)

    # Modulo complesso 2 
    modulo_scienza = ModuloComplesso("Modulo Scienza")
    modulo_scienza.aggiungi(sistema_ricerca)

    # Modulo complesso principale
    astronave_andromeda = ModuloComplesso("Astronave Andromeda")
    astronave_andromeda.aggiungi(modulo_composito)
    astronave_andromeda.aggiungi(modulo_scienza)

    # Avvio operazione
    astronave_andromeda.operazione()