"""
Faça um programa que leia um número inteiro positivo n e calcule
a soma dos n primeiros números naturais.
"""

soma = 0

numero = int(input('Digite um número: '))
for n in range(0, numero + 1):
    if numero > 0:
        soma = soma + n
    else:
        print('Número deve ser positivo.')
        numero = int(input('Digite um número: '))
print(soma)
