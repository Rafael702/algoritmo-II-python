import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from comum.estruturas import Pilha

p = Pilha()
num = 13

while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

while not p.empty():
    print(p.pop())
