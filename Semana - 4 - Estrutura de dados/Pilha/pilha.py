class Pilha():
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.empty():
            raise IndexError('pop em pilha vazia')
        self.top()
        return self.data.pop(-1)
        
    def top(self):
        if self.empty():
            raise IndexError('top em pilha vazia')
        print(self.data[-1])
        return self.data[-1]

    def empty(self):
        return not len(self.data) > 0


if __name__ == '__main__':
    p = Pilha()
    p.push(4)
    p.push(5)
    p.push(6)

    #6
    p.pop()
    #5
    p.pop()
    #4
    p.pop()
