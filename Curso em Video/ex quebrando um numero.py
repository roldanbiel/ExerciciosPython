
from math import trunc

# Maneira 01

num = float(input('Digite um valor: '))
print('Valor digitado é {} e sua porção inteira é {}.'.format(num, trunc(num)))

# Maneira 02

numero = float(input('Digite um valor: '))
print('Valor digitado é {} e sua porção inteira é {}.'.format(numero, int(numero)))
