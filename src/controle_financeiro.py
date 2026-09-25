from receita import Receita
from despesa import Despesa


class ControleFinanceiro:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionarTransacao(self, transacao):
        self._transacoes.append(transacao)

    def listarTransacoes(self):
        return self._transacoes

    def calcularSaldo(self):
        return sum(transacao.calcularImpacto() for transacao in self._transacoes)

    def calcularTotalReceitas(self):
        return sum(
            transacao.valor
            for transacao in self._transacoes
            if isinstance(transacao, Receita)
        )

    def calcularTotalDespesas(self):
        return sum(
            transacao.valor
            for transacao in self._transacoes
            if isinstance(transacao, Despesa)
        )

    def verificarSituacao(self):
        saldo = self.calcularSaldo()

        if saldo > 0:
            return "Saldo positivo"
        elif saldo < 0:
            return "Saldo negativo"
        else:
            return "Saldo equilibrado"