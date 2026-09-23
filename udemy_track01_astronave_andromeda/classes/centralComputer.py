import sys 
import time

# Pattern SINGLETON

class Computer():
    _istanza = None
    def __new__(cls):
        if cls._istanza is None:
            cls._istanza = super().__new__(cls)
            cls._istanza.stato = "In Attesa"
            cls._istanza.motori = "Spenti"
        return cls._istanza
        
    def statoAstronave(cls):
        print(f"Stato astronave: {cls.stato}. \nStato motori: {cls.motori}.")
    def avviaAstronave(cls):
        """Display progress bar while ship is turning on"""
        i = 1
        print("[LOG]: Controllo stato motori.....\n")
        time.sleep(10)
        print("[LOG]: OK => AVVIO MOTORI....")
        for i in range(101):
            percent = i / 101
            filled = int(40 * percent)
            bar = "=" * filled + "-" * (40 - filled)
            sys.stdout.write(f"\r|{bar}| {percent:.0%}")
            sys.stdout.flush()
        print("\n[LOG]: Motori accesi! Astronave in movimento")
        cls.motori = "Accesi"
        cls.stato = "In Movimento"

    def spegniAstronave(cls):
        """Display progress bar while ship is turning off"""
        i = 100
        print("[LOG]: Controllo stato motori.....\n")
        time.sleep(10)
        print("[LOG]: OK => Spegnimento Motori....")
        time.sleep(10)
        print("\n[LOG]: Motori spenti! Astronave in ferma")
        cls.motori = "Spenti"
        cls.stato = "In Attesa"

