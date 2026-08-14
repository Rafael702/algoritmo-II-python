class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)
    
    def remover(self):
        if self.empty():
            raise IndexError('remover em fila vazia')
        print(self.top())
        return self.data.pop(0)
    
    def top(self):
        if self.empty():
            raise IndexError('top em fila vazia')
        return self.data[0]

    def empty(self):
        return not len(self.data) > 0


if __name__ == '__main__':
    f = Fila()

    f.inserir(1)
    f.inserir(2)
    f.inserir(3)
    f.inserir(4)

    f.remover()
    f.remover()
    f.remover()
    f.remover()
