import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from comum.estruturas import Fila

f = Fila()

f.inserir(1)
f.inserir(2)
f.inserir(3)
f.inserir(4)

while not f.empty():
    print(f.remover())
