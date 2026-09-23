# grafo pesato 

class CorpoCeleste():
    def __init__(self, nome):
        self.nome = nome
        self.adiacenti = {}
    def aggiungi_collegamento(self, altro_corpo, distanza):
        self.adiacenti[altro_corpo] = distanza

    def rimuovi_collegamento(self, altro_corpo):
        if altro_corpo in self.adiacenti:
            del self.adiacenti[altro_corpo]
    def __str__(self):
        adiacenze = ",".join([f"{corpo.nome} (distanza: {distanza} UA)" for \
                              corpo, distanza in self.adiacenti.items()])
        return f"{self.nome} -> {adiacenze}"


class MappaStellare():
    def __init__(self):
        self.corpi_celesti = {}
    
    def aggiungi_corpo_celeste(self, nome):
        corpo = CorpoCeleste(nome)
        self.corpi_celesti[nome] = corpo
        return corpo
    def rimuovi_corpo_celeste(self, nome):
        if nome in self.corpi_celesti:
            for corpo in self.corpi_celesti.values():
                corpo.rimuovi_collegamento(self.corpi_celesti[nome])
            del self.corpi_celesti[nome]
    
    def aggiungi_percorso(self, nome_a, nome_b, distanza):
        if nome_a in self.corpi_celesti and nome_b in self.corpi_celesti:
            self.corpi_celesti[nome_a] \
            .aggiungi_collegamento(self.corpi_celesti[nome_b], distanza)
            self.corpi_celesti[nome_b]\
            .aggiungi_collegamento(self.corpi_celesti[nome_a], distanza)
    
    def __str__(self):
        return "\n".join(str(corpo) for corpo in self.corpu_celesti.values())
    
if __name__ == "__main__":
    pass