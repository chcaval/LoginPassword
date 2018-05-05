'''class mamifero:
    def __init__(self, cor_do_pelo, genero, andar):
        self.cor_do_pelo = cor_do_pelo
        self.genero = genero
        self.numero_de_patas = andar

    def falar(self):
        print('Ola, sou um mamifero e eu sei falar')

    def andar(self):
        print('Estou sobre {} patas'.format(self.numero_de_patas))

    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('Machos nao amamentam!')
            return
        print('Amamentando meu filhote.')


rex = mamifero('marrom', 'masculino', 4)
rex.falar()
rex.amamentar()
rex.andar()
'''

class Mamiferos:
    def __init__(self, cor_do_pelo, genero, andar):
        self.cor_do_pelo = cor_do_pelo
        self.genero = genero
        self.numeroDePatas = andar

    def falar(self):
        print('Eu sou um mamifero que fala!!')

    def corDoPelo(self):
        print('Meu pelo eh marrom')

    def Genero(self):
        if self.genero.lower()[0] == 'm':
            print('Nao posso amamentar')
        else:
            print('Estou amamentando')

    def andar(self):
        print('Estou sobre {} patas'.format(self.numeroDePatas))


thor = Mamiferos('marrom', 'macho', 4)
thor.corDoPelo()
thor.Genero()
thor.andar()
thor.falar()

Julia = Mamiferos('Preto', 'feminino', 2)
Julia.andar()
Julia.Genero()
Julia.corDoPelo()











