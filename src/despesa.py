from transacao import Transacao


class Despesa(Transacao):

    def calcularImpacto(self):
        return -self.valor