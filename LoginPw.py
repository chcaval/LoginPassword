from tkinter import *

i = Tk()

'''
For this login/password window, the 
login = carlos
password = 123
'''


def b():
    if ent.get() == 'carlos' and ent2.get() == '123':
        texto3['text'] = 'Access Alowed!'

    else:
        texto3['text'] = 'Wrong Username or Password!'

    '''if ent.get() != 'carlos':
        texto3['text'] = 'Wrong Username!'

        if ent2.get() != '123':
            texto3['text'] = 'Wrong Password !'
        else:
            texto2['text'] = 'Access not Alowed!'

    else:
        texto3['text'] = 'Access Alowed!'
    '''

i.geometry('300x200')

i.title('Login and Password')

texto = Label(i, text='Username')
texto.pack()
ent = Entry(i)
ent.pack()

texto2 = Label(i, text='Password')
texto2.pack()
ent2 = Entry(i)
ent2.pack()

b = Button(i, text='Enter', command=b )
b.pack()

b2 = Button(i, text='Sair', command=quit)
b2.pack()

texto3 = Label(i, text='')
texto3.pack()

i.mainloop()
