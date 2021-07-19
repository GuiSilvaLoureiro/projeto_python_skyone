class Squad:
    def __init__(self, nome, techlead = None, devs = None):
        self.nome = nome
        self.techlead = techlead
        self.devs = []

    def incluir_techlead(self, techlead):
        self.techlead = techlead

    def incluir_dev(self, dev):
        self.devs.append(dev)
