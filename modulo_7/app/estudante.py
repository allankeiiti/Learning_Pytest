from datetime import datetime


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
