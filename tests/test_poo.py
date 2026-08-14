import pytest

from conftest import load_script


@pytest.fixture(scope='module')
def ex01():
    return load_script('Semana - 2 - POO/ex-01.py')


@pytest.fixture(scope='module')
def ex02():
    return load_script('Semana - 2 - POO/ex-02.py')


@pytest.fixture(scope='module')
def ex03():
    return load_script('Semana - 2 - POO/ex-03.py')


@pytest.fixture(scope='module')
def exercicio01():
    return load_script('Semana - 2 - POO/exercicio-01.py')


@pytest.fixture(params=['ex01', 'ex02'])
def Point(request):
    return request.getfixturevalue(request.param).Point


def test_point_defaults_to_origin(Point):
    assert Point().get() == (0, 0)


def test_point_setx_and_sety_accumulate(Point):
    p = Point()
    p.setx(5)
    p.sety(6)
    p.setx(1)
    assert p.get() == (6, 6)


def test_point_move_applies_both_offsets(Point):
    p = Point(1, 2)
    p.move(-3, 4)
    assert p.get() == (-2, 6)


def test_point_repr(Point):
    assert repr(Point(1, 2)) == '(1,2)'


def test_point_add_two_points(ex02):
    result = ex02.Point(1, 2) + ex02.Point(3, 4)
    assert isinstance(result, ex02.Point)
    assert result.get() == (4, 6)


def test_point_add_scalar(ex02):
    assert (ex02.Point(2, 3) + 8).get() == (10, 11)


def test_point_add_does_not_mutate_operands(ex02):
    p = ex02.Point(1, 1)
    q = ex02.Point(2, 2)
    p + q
    assert (p.get(), q.get()) == ((1, 1), (2, 2))


def test_mylist_inherits_from_list(ex03):
    l = ex03.MyList([1, 2, 3])
    assert isinstance(l, list)
    l.append(4)
    assert l == [1, 2, 3, 4]


def test_mylist_choise_returns_member(ex03):
    values = [1, 2, 3, 4, 5, 6]
    l = ex03.MyList(values)
    assert all(l.choise() in values for _ in range(20))


def test_funcionario_repr_holds_attributes(exercicio01):
    f = exercicio01.funcionario('John', '23/05/2001', 1500)
    assert (f.nome, f.dtAdmissao, f.salario) == ('John', '23/05/2001', 1500)
    assert repr(f) == '(Nome:John,Data de Admissao:23/05/2001,Salario:R$1500)'


def test_gerente_is_a_funcionario(exercicio01):
    g = exercicio01.gerente('Bensom', '01/01/1990', 4500)
    assert isinstance(g, exercicio01.funcionario)


def test_gerente_bonus_adds_twenty_percent(exercicio01):
    g = exercicio01.gerente('Bensom', '01/01/1990', 4500)
    g.bonus()
    assert g.salario == pytest.approx(5400)
    g.bonus()
    assert g.salario == pytest.approx(6480)


def test_seguranca_keeps_funcionario_attributes(exercicio01):
    s = exercicio01.seguranca('Aroldo', '25/11/1985', 2600)
    assert isinstance(s, exercicio01.funcionario)
    assert not hasattr(s, 'bonus')
    assert s.salario == 2600
