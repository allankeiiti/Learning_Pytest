"""
    Utilizando os Markers

    Com pytest.mark podemos facilimente setar metadatas para nossas funções

    as markers utilizadas aqui foram:
    - mark.skip (Pula a função de teste)
    - mark.skipif (Pula a função de teste caso determinada condição seja atendida)
    - mark.xfail (Quando um erro no teste é esperado por tal motivo especificado, no exemplo deste código
                  é por conta do teste estar sendo feito no windows (win32))
"""

import pytest
import sys


def adicionar_valores(a, b):
    return a + b


# Caso queremos ignorar uma função na hora de executar o pytest usamos a Marker skip
@pytest.mark.skip(reason='Quero ignorar esse teste')
def test_adicionar_valores():
    """
        ITEM 1
        Função utilizada para realizar testes da função adicionar_valores()
        Execute este script com o 'pytest modulo_1.py' no console
    :return:
    """
    assert adicionar_valores(2, 3) == 5


# Caso queremos dar um skip seguindo uma condição usamos a Marker skipif
@pytest.mark.skipif(sys.version_info > (3, 6), reason='Use python 3.6 ou abaixo')
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
    # XFAIL ignora se uma exceção é invocada
    # Se estou testando no windows, o teste ignora a função - Se fosse no linux colocariamos sys.platform == 'linux'
    @pytest.mark.xfail(sys.platform == "win32", reason='Não execute isso no Windows')
    def test_allan(self):
        """
            ITEM 3
        :return:
        """
        assert adicionar_valores('c', 'd') == 'cd'
        raise Exception()

    def test_list(self):
        """
            ITEM 4
        :return:
        """
        assert adicionar_valores([1, 2], [3, 4]) == [1, 2, 3, 4]