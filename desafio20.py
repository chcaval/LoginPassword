import random

n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third Student: '))
n4 = str(input('Fourth Student: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('O aluno escolhido foi: {}'.format(lista))