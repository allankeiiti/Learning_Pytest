"""
    Software test fixtures
"""

import json
import os


def save_dict(_dict, filepath):
    json.dump(_dict, open(filepath, 'w'))
    print('salvo')


def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, 'test.json')
    dict = {'a': 1, 'b': 2}
    save_dict(_dict=dict, filepath=filepath)
    # Verificando se o arquivo salvo é o mesmo que a variável 'd'
    assert json.load(open(filepath, 'r')) == dict
    # Verifica se foi printado o 'salvo' que ocorre ao chamar a função save_dict()
    # e é incluso o '\n' por conta que a cada print do python uma linha é quebrada
    assert capsys.readouterr().out == 'salvo\n'
