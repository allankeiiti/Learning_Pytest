"""
    Aqui temos funções cujo possuem condições que caso sejam ou não atendidas, um erro é invocado e isso é esperado.

    Portanto aqui é utilizado o pytest.raises(<Tipo de Erro>) para falar pro Pytest que este erro é esperado e que deve
    ser invocado. Pois quando é testado um software também é necessário tentar quebrá-lo e ver como ele se comporta.
"""
import pytest


def validar_idade(idade: int):
    if isinstance(idade, int):
        if idade < 0:
            raise ValueError(f'O valor passado: {idade} é inválido (Valor menor que 0)')
    else:
        raise ValueError(f'O valor passado: {idade}, não é um inteiro, por favor passe um valor do tipo Integer')


def test_validar_idade_valida():
    """
        Item 1
    :return:
    """
    validar_idade(10)


def test_validar_idade_nao_valida():
    """
        Item 2
    :return:
    """
    with pytest.raises(ValueError):
        validar_idade(-1)


def test_validar_idade_string():
    """
        Item 3
    :return:
    """
    with pytest.raises(ValueError):
        validar_idade('allan')

