n = str(input('Enter a name: ')).strip().lower()
print("Quantas vezes appears the letter 'a'? {}".format(n.count('a')))
print("Quantas vezes appears the letter 'a'? {}".format(n.find('a')+1))
print("Quantas vezes appears the letter 'a'? {}".format(n.rfind('a')+1))
print("Quantas vezes appears the letter 'a'? {}".format(len(n)-n.count(' ')))

