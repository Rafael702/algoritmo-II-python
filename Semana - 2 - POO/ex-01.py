class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x += x

    def sety(self, y):
        self.y += y

    def get(self):
        return self.x, self.y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    #Semelhante ao toString(), ao inves de retornar o endereço de memoria do objeto, ele retorna os valores do objeto
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


p = Point()
p.setx(5)
p.sety(6)
print(p)