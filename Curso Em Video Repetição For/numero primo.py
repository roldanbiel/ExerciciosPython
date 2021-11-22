
numero = int(input('Informe um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[32m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[33m\nO número {} foi divisível {} vezes'.format(numero, total), end='')
if total == 2:
    print(' e por isso ele é um número primo.')
else:
    print(' e por isso ele não é um número primo.')
