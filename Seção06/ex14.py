"""
Faça um programa que leia um número inteiro positivo par N
e imprima todos os números pares de 0 até N em ordem decrescente.
"""

numero = int(input('Digite um número: '))

for n in range(numero, -1, -2):
    if numero % 2 == 0:
        print(n)
    else:
        print('Valor precisa ser par.')
        numero = int(input('Digite um número: '))
