"""
    Utilizando o assert:

    É utilizado o assert para verificar se tal variável é determinado valor, como se fosse um if else

    x = 10
    if x == 10:
        print('certo')

    assert x == 10

    Com o IF, caso a condição não seja atendida ele não vai cair nos comandos dentro da condição,
    já no assert, um AssertionError é invocado

    executando este script com o pytest, ele irá retornar uma quantidade de 'Items' coletados,
    sendo esses itens as funções com o prefixo 'test_' inseridas em seu nome
"""


def adicionar_valores(a, b):
    return a + b


def test_adicionar_valores():
    """
        ITEM 1
        Função utilizada para realizar testes da função adicionar_valores()
        Execute este script com o 'pytest modulo_1.py' no console
    :return:
    """
    assert adicionar_valores(2, 3) == 5


def test_adicionar_valores_str():
    """
        ITEM 2
        Função utilizada para realizar testes da função adicionar_valores() com string
        Execute este script com o 'pytest modulo_1.py' no console
    :return:
    """
    assert adicionar_valores('a', 'b') == 'ab'


class TestSample:
    """
        Classe que contém demais métodos de teste.
    """
    def test_allan(self):
        """
            ITEM 3
        :return:
        """
        assert adicionar_valores('c', 'd') == 'cd'

    def test_list(self):
        """
            ITEM 4
        :return:
        """
        assert adicionar_valores([1, 2], [3, 4]) == [1, 2, 3, 4]