"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior
deles e quantas vezes o maior número foi lido. A quantidade de números a serem
lidos deve ser fornecido pelo usuário.
"""

maior = -999
menor = 999
vezes = 0
qtd = int(input('Quantos números quer informar: '))

for n in range(0, qtd):
    numero = int(input('Digite um número: '))
    if numero >= maior:
        maior = numero
        vezes = vezes + 1
    elif numero < menor:
        menor = numero
print('Maior:', maior)
print('Menor:', menor)
print('O maior número foi lido:', vezes, 'vezes.')
