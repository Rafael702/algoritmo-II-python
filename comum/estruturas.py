"""Estruturas de dados basicas usadas nos exemplos das aulas."""


class Fila:
    """Fila FIFO: insere no fim e remove do inicio."""

    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)

    def remover(self):
        if self.empty():
            return None
        return self.data.pop(0)

    def top(self):
        if self.empty():
            return None
        return self.data[0]

    def empty(self):
        return len(self.data) == 0


class Pilha:
    """Pilha LIFO: insere e remove no topo."""

    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.empty():
            return None
        return self.data.pop(-1)

    def top(self):
        if self.empty():
            return None
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0
