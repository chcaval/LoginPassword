n1 = float(input('Note 1: '))
n2 = float(input('Note 2: '))
m = (n1+n2)/2

if m>=6:
    print('You got a good grade = {}. Congrats'.format(m))
else:
    print("You didn't get good score. {}".format(m))
