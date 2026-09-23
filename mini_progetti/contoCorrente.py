
class Conto():
    def __init__(self, nome: str, conto: str):
        self.nome = nome
        self.conto = conto
    
class ContoCorrente(Conto):
    def __init__(self, nome: str, conto: str, importo: int):
        super().__init__(nome, conto)
        self.__saldo = importo
    def preleva(self, importo):
        self.__saldo = self.__saldo - importo
    def deposita(self, importo):
        self.__saldo = self.__saldo + importo
    def descrizione(self):
        print("Il titolare: " + self.nome + " del conto " + self.conto + " ha un saldo di " + str(self.__saldo))
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

class GestoreContiCorrenti():
    @staticmethod
    def bonifico(sorgente: ContoCorrente, destinazione: ContoCorrente, importo: int):
        sorgente.preleva(importo)
        destinazione.deposita(importo)


if __name__ == "__main__":
    c1 = ContoCorrente("Mario Rossi", "CLCFPP01S06F784I", 1000)
    c1.deposita(100)
    c1.descrizione()
    print(c1.saldo)
    print("Post deposito\n")
    c1.preleva(10)
    c1.descrizione()
    print("Post prelievo\n")

    c2 = ContoCorrente("Luigi verdi", "ABCDEFGHILMNO", 2000)
    c2.descrizione()

    print("\n")
    print("Eseguo bonifico : \n")
    GestoreContiCorrenti.bonifico(c1, c2, 1090)
    c1.descrizione()
    c2.descrizione()
    print("Post prelievo\n")