from transacao import Transacao

class Receita(Transacao):

    def calcularImpacto(self):
        return self.valor