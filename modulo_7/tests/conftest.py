from datetime import datetime

import pytest

from modulo_7.app.estudante import Estudante


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
def criar_estudante_dummy():
    def _criar_estudante_dummy(nome, creditos):
        return Estudante(nome=nome,
                         dob=datetime(2000, 1, 1),
                         branch='coe',
                         creditos=creditos)

    return _criar_estudante_dummy
