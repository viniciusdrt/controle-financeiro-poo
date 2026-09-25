class Categoria:
    def __init__(self, nome, descricao):
        self._nome = nome
        self._descricao = descricao

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    def __str__(self):
        return self._nome
