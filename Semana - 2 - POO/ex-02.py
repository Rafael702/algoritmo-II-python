# Sobrecarga de Operadores
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.geometria import Point

p = Point(1, 2)
print(p)
q = Point(3, 4)
print(p + q)
print(p + 2)
