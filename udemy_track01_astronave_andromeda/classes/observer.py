from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def aggiorna(self, status:bool ):
        pass


class Subject(ABC):
    def __init__(self):
        self._observers = []
    
    def add_obs(self, observer: Observer):
        self._observers.append(observer)
    
    def rm_obs(self, observer: Observer):
        self._observers.remove(observer)
    def up_obs(self, status:bool):
        for observer in self._observers:
            observer.update(status)


class SistemaDiAllarme(Subject):
    def __init__(self):
        super().__init__()
        self._isActive = False
    def active(self):
        self._isActive = True
        self.up_obs(self._is_active)
    def deActive(self):
        self._isActive = False
        self.up_obs(self._isActive)


class PonteComando(Observer):
    def up_obs(self, status: bool):
        if status == True:
            print("Ponte di comando:  Avvio blocco porte ")
        else:
            print("Ponte di comando: Sblocco porte")

class cabineEquipaggio(Observer):
    def up_obs(self, status: bool):
        if status == True:
            print("Cabine equipaggio:  Avvio blocco porte ")
        else:
            print("Cabine equipaggio: Sblocco porte")

   
# Pattern Observer
if __name__ == "__main__":
    pass