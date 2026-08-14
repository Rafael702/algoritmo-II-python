import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.demo import demonstrar_ordenacao


def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and x < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = x


demonstrar_ordenacao('Insertion sort', insertion_sort, [44, 55, 12, 42, 94, 18, 6, 67])
