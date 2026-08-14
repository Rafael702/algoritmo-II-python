import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.demo import demonstrar_ordenacao


def quick_sort(v, ini, fim):
    meio = (ini + fim) // 2
    pivo = v[meio]
    i = ini
    j = fim
    while i < j:
        while v[i] < pivo:
            i += 1
        while v[j] > pivo:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1
    if j > ini:
        quick_sort(v, ini, j)
    if i < fim:
        quick_sort(v, i, fim)


demonstrar_ordenacao(
    'Quick sort',
    lambda v: quick_sort(v, 0, len(v) - 1),
    [25, 57, 35, 37, 12, 86, 92, 33],
)
