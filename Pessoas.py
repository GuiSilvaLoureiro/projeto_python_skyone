class Pessoa:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

    def exibir(self):
        print(f'-> {self.nome} - {self.fone}')
