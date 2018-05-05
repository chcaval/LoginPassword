class geometrico():
    def __init__(self, n, l):
        self.nome = n
        self.lado = l
        print('Construtor criado com sucesso!! Congrats!!')

    def imp(self):
        print('A nova figura eh um {} e o seu lado mede: {}'.format(self.nome, self.lado))
        print('Sua area eh: {}'.format(self.lado**2))


a = geometrico('quadrado', 6)
a.imp()





''' lado = int(input('Enter valor do lado do quadrado: '))
        print('O nome da figura eh {} e o seu lado eh: {}'.format('quadrado', lado ))
        retornar lado * lado
        print('Sua area eh {}'.format(lado * lado)
        
class Meu_Objeto:
    def __init__(self):
        self.nome = 'Carlos'
        self.idade = 45
        print('Construtor criado com sucesso!! Congrats!!')

    def imprimir(self):
        print('Meu nome eh {} e minha idade eh: {}'.format('Carlos', 45))
Carlos = Meu_Objeto()
Carlos.imprimir()'''
