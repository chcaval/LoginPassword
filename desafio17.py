from math import hypot
c1 = int(input('entre a number: '))
c2 = int(input('Entre another number: '))
#h = c1*c1 + c2*c2
#print('The hypotenuse is {}'.format(h**0.5))

h = math.hypot(c1, c2)
print('The hypotenuse is {}'.format(h))

