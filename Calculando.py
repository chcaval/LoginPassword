from tkinter import *
#import shelve


'''class Calculando(object):
    def __init__(self, usuario, senha, botao):
        self.usuario = usuario
        self.senha = senha
        self.botao = botao
'''
def calcular():

    #resultado['text'] = 'Calculando'

    a = Tk()

    a.title('Calculando')

    a.geometry('220x150')

    #Area de texto Usuario
    texto = Label(a, text='Usuario')
    texto.pack()
    ent = Entry(a)
    ent.pack()

    #Area de texto Senha
    texto1 = Label(a, text='Senha')
    texto1.pack()
    ent1 = Entry(a)
    ent1.pack()

    #Botao Entrar
    calc = Button(a, text='Entrar', command=calcular)
    calc.pack()


    #Texto das formulas:
    '''if ent == '':
        resultado = Label(a, text='')
        resultado.pack()
        resultado['text'] = ent.get()


    elif ent == 'Carlos':
        resultado = Label(a, text='Bem vindo Carlos', fg='green')
        resultado.pack()
        resultado['text'] = ent.get()
    else:
        resultado = Label(a, text='Nome invalido', fg='Red')
        resultado.pack()
        resultado['text'] = ent.get()'''

    a.mainloop()
