# Herancas
import random

#(list) -> Forma de realizar a heranca
class MyList(list):
    def choise(self):
        return random.choice(self)

l = MyList([1,2,3,4,5,6])
print(l)
print(len(l))
l.append(5)
print(l)
print(l.choise())