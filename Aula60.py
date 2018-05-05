class Pessoa:
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao

    def treinar(self):
        self.cao.daPatinha()
        self.cao.latir()


class Cachorro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def daPatinha(self):
        print('{} extendeu a patinha.'.format(self.nome))

    def latir(self):
        print('Auauauauau')


rex = Cachorro('Rex', 'marrom')
Carlos = Pessoa('Carlos', 70, rex)

Carlos.cao.daPatinha()
Carlos.cao.latir()
