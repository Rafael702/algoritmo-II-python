import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.demo import demonstrar_ordenacao


def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        intercala(v, ini, meio, fim)


def intercala(v, ini, meio, fim):
    L = v[ini:meio + 1]
    R = v[meio + 1:fim + 1]
    # sentinelas - valor maximo - evita que a incrementacao ultrapasse os indices validos
    L.append(999)
    R.append(999)
    i = 0
    j = 0
    for k in range(ini, fim + 1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1


demonstrar_ordenacao(
    'Merge sort',
    lambda v: merge_sort(v, 0, len(v) - 1),
    [5, 2, 4, 7, 1, 3, 2, 6],
)
