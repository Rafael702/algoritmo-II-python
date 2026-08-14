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

    # Semelhante ao toString(): retorna os valores do objeto e nao o endereco de memoria
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    # (2,3) + (2,2) => (4,5) | (2,3) + 8 => (10,11)
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return Point(self.x + other, self.y + other)
