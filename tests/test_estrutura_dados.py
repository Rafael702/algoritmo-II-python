import subprocess
import sys

import pytest

from conftest import REPO_ROOT, load_script

PILHA = 'Semana - 4 - Estrutura de dados/Pilha/pilha.py'
FILA = 'Semana - 4 - Estrutura de dados/Filas/filas.py'
FILA_PILHA = 'Semana - 4 - Estrutura de dados/Pilha/filas.py'
BINARIO = 'Semana - 4 - Estrutura de dados/Pilha/binario.py'


@pytest.fixture(scope='module')
def Pilha():
    return load_script(PILHA).Pilha


@pytest.fixture(scope='module', params=[FILA, FILA_PILHA])
def Fila(request):
    return load_script(request.param, name='filas_' + request.param.split('/')[-2]).Fila


def test_pilha_starts_empty(Pilha):
    assert Pilha().empty() is True


def test_pilha_is_lifo(Pilha):
    p = Pilha()
    for x in (4, 5, 6):
        p.push(x)
    assert p.empty() is False
    assert [p.pop(), p.pop(), p.pop()] == [6, 5, 4]
    assert p.empty() is True


def test_pilha_top_prints_last_pushed_without_removing(Pilha, capsys):
    p = Pilha()
    p.push(1)
    p.push(2)
    p.top()
    assert capsys.readouterr().out == '2\n'
    assert p.data == [1, 2]


def test_pilha_pop_on_empty_raises(Pilha):
    with pytest.raises(IndexError):
        Pilha().pop()


def test_fila_starts_empty(Fila):
    assert Fila().empty() is True


def test_fila_is_fifo(Fila):
    f = Fila()
    for x in (1, 2, 3, 4):
        f.inserir(x)
    assert f.empty() is False
    assert [f.remover() for _ in range(4)] == [1, 2, 3, 4]
    assert f.empty() is True


def test_fila_top_returns_oldest_without_removing(Fila):
    f = Fila()
    f.inserir('a')
    f.inserir('b')
    assert f.top() == 'a'
    assert f.data == ['a', 'b']


def test_fila_remover_on_empty_raises(Fila):
    with pytest.raises(IndexError):
        Fila().remover()


def test_binario_prints_binary_representation_of_13():
    result = subprocess.run(
        [sys.executable, BINARIO],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.split()[-4:] == list('1101')
