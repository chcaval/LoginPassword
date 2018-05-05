#CreateArquivo = open('arquivo.txt')
#CreateArquivo.read('\nbom dia')

arquivo2 = open('arquivo2.txt', 'w')

arquivo2.write('Ciacao de um novo arquivo.')
arquivo2.write('\nHello my new file!!')
arquivo2.write('\nEstah funcionando!')
arquivo2.close()


arquivo2 = open('arquivo2.txt', 'r')
#print(arquivo2.read())
#print(arquivo2.readline(0))
#print(arquivo2.readlines())
#print(arquivo2.readline())

for i in range(3):
    a = arquivo2.readline()
    print(a)
arquivo2.close()

