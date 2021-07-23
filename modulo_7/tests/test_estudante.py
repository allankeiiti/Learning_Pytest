"""
    PyTest Fixture Factory

    - Fabricando Funções de teste

    https://medium.com/assertqualityassurance/tutorial-de-pytest-para-iniciantes-cbdd81c6d761

"""

from datetime import datetime
from modulo_7.app.estudante import get_topper


def test_estudante_get_idade(estudante_dummy):
    """
        ITEM 1
    :param estudante_dummy:
    :return:
    """
    estudante_dummy_idade = (datetime.now() - estudante_dummy.dob).days // 365
    assert estudante_dummy.get_idade() == estudante_dummy_idade


def test_student_get_creditos(estudante_dummy):
    """
        ITEM 3
    :param estudante_dummy:
    :return:
    """
    assert estudante_dummy.get_creditos() == 20


def test_get_topper(criar_estudante_dummy):
    estudantes = [
        criar_estudante_dummy(nome='Diego', creditos=30),
        criar_estudante_dummy(nome='Joao', creditos=50),
        criar_estudante_dummy(nome='Kaue', creditos=99)
    ]

    topper = get_topper(estudantes)

    assert topper == estudantes[2]

