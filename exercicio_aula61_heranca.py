class ObjetoGrafico(object):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno):
        self.cor_de_preenchimento = cor_de_preenchimento
        self.preenchida = preenchida
        self.cor_de_contorno = cor_de_contorno

    def printer(self):
        print('A cor eh: {}'.format(self.cor_de_preenchimento))


    def preencher(self):
         if self.preenchida.lower() == 'yes':
             print('True')
         else:
             print('False')

    def contornar(self):
        print('A cor de contorno eh {}'.format(self.cor_de_contorno))


'''figura = ObjetoGrafico(10, 'yes', 15)
figura.printer()
figura.contornar()
figura.preencher()
'''


class Retangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, base, altura):
        super(Retangulo, self).__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
        self.base = base
        self.altura = altura
        print(base*altura)

'''
class Circulo(ObjetoGrafico):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, raio):
        super(Circulo, self).__init__(15, 'no', 20)
        self.raio = raio


class Triangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno,base, altura):
        super(Triangulo, self).__init__(12, 'yes', 13)
        self.base = base
        self.altura = altura
'''

r = Retangulo(100, 'yes', 200, 5, 4)
r.base()
