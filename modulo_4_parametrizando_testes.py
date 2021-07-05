"""
    Parametrizando testes

    Ao invés de criar várias funções (ou objetos, segundo o pytest) podemos utilizar a parametrização
    de testes unitários com a Marker parametrize (pytest.mark.parametrize)
"""

import pytest


def adicionar_valores(a, b):
    return a + b


def test_adicionar_valores_int():
    """
        ITEM 1
        Função utilizada para realizar testes da função adicionar_valores()
        Execute este script com o 'pytest modulo_1.py' no console
    :return:
    """
    assert adicionar_valores(2, 3) == 5


def test_adicionar_valores_list():
    """
        ITEM 2
        Função utilizada para realizar testes da função adicionar_valores() com listas
        Execute este script com o 'pytest modulo_1.py' no console
    :return:
    """
    assert adicionar_valores([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_adicionar_valores_str():
    """
        ITEM 3
        Função utilizada para realizar testes da função adicionar_valores() com string
        Execute este script com o 'pytest modulo_1.py' no console
    :return:
    """
    assert adicionar_valores('a', 'b') == 'ab'


# função parametrizada
@pytest.mark.parametrize('a, b, c',
                         [(2, 3, 5),
                          ([1, 2], [3, 4], [1, 2, 3, 4]),
                          ('a', 'b', 'ab')],
                         ids=['int', 'list', 'str'])
def test_adicionar_valores(a, b, c):
    assert adicionar_valores(a, b) == c
