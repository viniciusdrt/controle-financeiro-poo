from abc import ABC, abstractmethod
from datetime import date


class Transacao(ABC):
    def __init__(self, descricao, valor, data, categoria):
        self._descricao = descricao
        self._valor = valor
        self._data = data
        self._categoria = categoria

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @abstractmethod
    def calcularImpacto(self):
        pass