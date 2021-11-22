
numero = int(input('Informe um número para ver sua tabuada: '))

for c in range(1, 11):
    print('{} X {} = {}'.format(numero, c, numero * c))
