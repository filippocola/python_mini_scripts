# Desing pattern Factory Method pattern
from abc import ABC, abstractmethod

# Product 
class ModuloSpaziale:
    def __init__(self, nome, tipo, funzione):
        self.nome = nome
        self.tipo = tipo
        self.funzione = funzione


# Concrete Products
class ModuloEsplorazione(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Esplorazione", "Esplorazione", "Esplorare nuovi settori spaziali")

class ModuloDifesa(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Difesa", "Difesa", "Sistema di difesa avanzato intergalattico")

class ModuloRicerca(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Ricerca", "Ricerca", "Sistema di ricerca avanzato")

class ModuloSupportoVitale(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo di supporto vitale", "Supporto", "Tiene in vita l'equipaggio")

# Creator
class Creator(ABC):
    @abstractmethod
    def crea_modulo(self, tipo_modulo):
        pass

# Concreate Creator 
class FactoryModuliSpaziali(Creator):
    def crea_modulo(self, tipo_modulo):
        if (tipo_modulo.lower() == "esplorazione"):
            return ModuloEsplorazione()
        if (tipo_modulo.lower() == "difesa"):
            return ModuloDifesa()
        if (tipo_modulo.lower() == "ricerca"):
            return ModuloRicerca()
        if (tipo_modulo.lower() == "supporto"):
            return ModuloSupportoVitale()
        else: 
            ValueError(f"Tipo modulo non valido: {tipo_modulo}")

if __name__ == "__main__":
    factory = FactoryModuliSpaziali()

    modulo_esplorazione = factory.crea_modulo("Esplorazione")
    print(f"Modulo creato: {modulo_esplorazione.name}")

    modulo_difesa = factory.crea_modulo("Difesa")
    print(f"Modulo creato: {modulo_difesa.nome}")

    modulo_ricerca = factory.crea_modulo("Ricerca")
    print(f"Modulo Creato: {modulo_ricerca.nome}")

    try:
        factory.crea_modulo("Non valido")
    except Exception as e:
        print(f"Errore: {e}")