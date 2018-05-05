from tkinter import *


def soma():
    if (str(entrada1.get()).isnumeric() and str(entrada2.get()).isnumeric()):
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        resultado['text']= num1 + num2
    else:
        resultado['text'] = 'O valor digitado nao eh um numero! \nTente outra vez, por favor.'


janela = Tk()
janela.geometry('250x250')

texto1 = Label(janela, text='Primeira parcela:')
texto1.pack()
entrada1 = Entry(janela)
entrada1.pack()

texto2 = Label(janela, text='Segunda parcela:')
texto2.pack()
entrada2 = Entry(janela)
entrada2.pack()

bt_soma = Button(janela, text='Soma', command=soma)
bt_soma.pack()

resultado = Label(janela, text="")
resultado.pack()


janela.mainloop()