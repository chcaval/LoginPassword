from tkinter import *

i = Tk()

i.geometry('800x600')

#Titulo da Tela
i.title('Calculadora para Estatistica')

#Dar um icone
#i.wm_iconbitmap('Icone.ico')


texto = Label(i, text='Usuario')
texto.pack()

#Area ou zona de texto
ent = Entry(i)
ent.pack()

texto = Label(i, text = 'Senha')
texto.pack()
ent = Entry(i)
ent.pack()

#ciracao de um botao

b = Button(i, text='Entrar')
b.pack()

b2 = Button(i, text ='Sair', command=quit)
b2.pack()


i.mainloop()