import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.geometria import Point

p = Point()
p.setx(5)
p.sety(6)
print(p)
