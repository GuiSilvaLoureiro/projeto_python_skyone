from projeto_python_skyone.Colaboradores import Colaborador


class Dev(Colaborador):
    def __init__(self, nome, fone, cargo, squad = None):
        super().__init__(nome, fone, squad)
        self.cargo = cargo

    def exibir(self):
        super().exibir()
        print(f'   Cargo de {self.cargo} na squad {self.squad.nome}\n')
