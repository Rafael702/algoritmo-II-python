import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from comum.estruturas import Pilha

p = Pilha()
p.push(4)
p.push(5)
p.push(6)

# 6, 5, 4
while not p.empty():
    print(p.pop())
