import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.demo import demonstrar_ordenacao


def bubble_sort(v):
    for i in range(len(v) - 1):
        for j in range(len(v) - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]


demonstrar_ordenacao('Bubble sort', bubble_sort, [24, 48, 92, 37, 12, 57, 86, 33])
