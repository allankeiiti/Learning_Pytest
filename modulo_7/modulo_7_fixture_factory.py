"""
    PyTest Fixture Factory

    - Fabricando Funções de teste

    https://medium.com/assertqualityassurance/tutorial-de-pytest-para-iniciantes-cbdd81c6d761

"""


from datetime import datetime
import pytest


class Estudante:
    def __init__(self, nome, dob, branch, creditos):
        self.nome = nome
        self.dob = dob
        self.branch = branch
        self.creditos = creditos

    def get_idade(self):
        return (datetime.now() - self.dob).days // 365

    def get_creditos(self):
        return self.creditos


def get_topper(estudantes):
    return max(estudantes, key=lambda estudante: estudante.get_creditos())


@pytest.fixture
def estudante_dummy():
    """
        Essa Fixture permite a criação de um estudante Dummy para testes
    :return: Estudante Object
    """
    return Estudante(nome='Allan K.',
                     dob=datetime(2000, 1, 1),
                     branch='coe',
                     creditos=20)


# Criando a Fixture Factory de Estudantes Dummies
@pytest.fixture
def dummy_estudante_factory():
    def criar_estudante_dummy(nome, creditos):
        return Estudante(nome=nome,
                         dob=datetime(2000, 1, 1),
                         branch='coe',
                         creditos=creditos)

    return criar_estudante_dummy


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
