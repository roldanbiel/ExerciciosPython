
i = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
dec = i + (10 - 1) * r
for c in range(i, dec + r, r):
    print('{} '.format(c), end='> ')
print('FIM!')
