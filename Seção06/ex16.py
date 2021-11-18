"""
Faça um programa que leia um número inteiro positivo ímpar N
e imprima todos os números pares de 1 até N em ordem decrescente.
"""

numero = int(input('Digite um número: '))

for n in range(numero, -1, -2):
    if numero % 2 == 1:
        print(n)
    else:
        print('Valor precisa ser ípar.')
        numero = int(input('Digite um número: '))
