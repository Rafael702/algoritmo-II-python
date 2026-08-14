import random

import pytest

from conftest import load_script

CASES = [
    [],
    [1],
    [2, 1],
    [24, 48, 92, 37, 12, 57, 86, 33],
    [5, 5, 5],
    [-3, 10, -3, 0, 7],
]


@pytest.fixture(scope='module')
def bubble():
    return load_script('Semana 5 - Ordenacao/bubble_sort.py').buble_sort


@pytest.fixture(scope='module')
def insertion():
    return load_script('Semana 5 - Ordenacao/insertion_sort.py').insertion_sort


@pytest.fixture(scope='module')
def merge():
    return load_script('Semana 5 - Ordenacao/merge_sort.py')


@pytest.fixture(scope='module')
def quick():
    return load_script('Semana 5 - Ordenacao/quick_sort.py').quick_sort


@pytest.mark.parametrize('values', CASES)
def test_buble_sort_orders_in_place(bubble, values, capsys):
    v = list(values)
    assert bubble(v) is None
    assert v == sorted(values)
    assert capsys.readouterr().out.strip() == str(sorted(values))


@pytest.mark.parametrize('values', CASES)
def test_insertion_sort_orders_in_place(insertion, values):
    v = list(values)
    assert insertion(v) is None
    assert v == sorted(values)


@pytest.mark.parametrize('values', [c for c in CASES if c])
def test_merge_sort_orders_in_place(merge, values):
    v = list(values)
    merge.merge_sort(v, 0, len(v) - 1)
    assert v == sorted(values)


@pytest.mark.parametrize('values', [c for c in CASES if c])
def test_quick_sort_orders_in_place(quick, values):
    v = list(values)
    quick(v, 0, len(v) - 1)
    assert v == sorted(values)


def test_intercala_merges_two_sorted_halves(merge):
    v = [1, 4, 9, 2, 3, 8]
    merge.intercala(v, 0, 2, 5)
    assert v == [1, 2, 3, 4, 8, 9]


def test_merge_sort_leaves_single_element_untouched(merge):
    v = [7]
    merge.merge_sort(v, 0, 0)
    assert v == [7]


def test_sorts_agree_on_random_input(bubble, insertion, merge):
    rng = random.Random(7)
    values = [rng.randint(-50, 50) for _ in range(30)]
    expected = sorted(values)

    for sort in (
        lambda v: bubble(v),
        lambda v: insertion(v),
        lambda v: merge.merge_sort(v, 0, len(v) - 1),
    ):
        v = list(values)
        sort(v)
        assert v == expected


@pytest.mark.xfail(
    reason='intercala uses 999 as sentinel, so values >= 999 overrun the halves',
    raises=IndexError,
    strict=True,
)
def test_merge_sort_handles_values_above_the_sentinel(merge):
    v = [5000, 1000, 2]
    merge.merge_sort(v, 0, 2)
    assert v == [2, 1000, 5000]


@pytest.mark.xfail(
    reason='partition advances i and j even when they already crossed, '
           'skipping one element',
    strict=True,
)
def test_quick_sort_orders_when_partition_indexes_cross(quick):
    values = [33, -2, 50, -24, -38, 12, -47, -1, 5]
    v = list(values)
    quick(v, 0, len(v) - 1)
    assert v == sorted(values)
