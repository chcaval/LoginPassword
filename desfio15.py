from math import trunc

n = float(input('Enter a number: '))
k = n//1
print('The integer part is: {}'.format(k))

m = float(input('Enter a number: '))
print('The number {} portion integer is {}'.format(m, trunc(m)))



