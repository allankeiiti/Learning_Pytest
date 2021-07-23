"""
    Custom Software test fixtures

    - Utilizado a fixture pytest.fixture.function
"""

from datetime import datetime
import pytest


class Estudante:
    def __init__(self, nome, dob, branch):
        self.nome = nome
        self.dob = dob
        self.branch = branch
        self.creditos = 0

    def get_idade(self):
        return (datetime.now() - self.dob).days // 365

    def add_creditos(self, valor):
        self.creditos += valor

    def get_creditos(self):
        return self.creditos


@pytest.fixture(scope="function")
def estudante_dummy():
    """
        Essa Fixture permite a criação de um estudante Dummy para testes
    :return: Estudante Object
    """
    print('Criando estudante Dummy')
    return Estudante("Allan", datetime(1997, 12, 7), 'coe')


def test_estudante_get_idade(estudante_dummy):
    """
        ITEM 1
    :param estudante_dummy:
    :return:
    """
    estudante_dummy_idade = (datetime.now() - estudante_dummy.dob).days // 365
    assert estudante_dummy.get_idade() == estudante_dummy_idade


def test_student_add_creditos(estudante_dummy):
    """
        ITEM 2
    :param estudante_dummy:
    :return:
    """
    estudante_dummy.add_creditos(5)
    assert estudante_dummy.get_creditos() == 5


def test_student_get_creditos(estudante_dummy):
    """
        ITEM 3
    :param estudante_dummy:
    :return:
    """
    assert estudante_dummy.get_creditos() == 0
