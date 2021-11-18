"""
Faça um programa que leia 10 números inteiros e imprima sua média.
"""

media = 0
soma = 0
for n in range(1, 11):
    numeros = int(input('Digite um valor: '))
    soma = soma + numeros
    media = soma / 10
print('Média:', media)
