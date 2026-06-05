from pilha import Pilha

p = Pilha()
num = 13

while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

while not p.empty():
    p.pop()