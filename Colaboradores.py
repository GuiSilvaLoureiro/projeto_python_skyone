from projeto_python_skyone.Pessoas import Pessoa


class Colaborador(Pessoa):
    def __init__(self, nome, fone, squad = None):
        super().__init__(nome, fone)
        self.squad = squad

    def incluir_squad(self, squad):
        self.squad = squad
