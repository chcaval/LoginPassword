n = int(input('Enter a number smaller than 10: '))
aux = n
dig = reverso = 0

while aux != 0:
    dig = aux%10
    reverso = reverso*10 + dig
    aux //= 10
if reverso == n:
    print('{} eh palindromo!'.format(n))
else:
    print('{} nao eh palindromo!'.format(n))