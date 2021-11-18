"""
Faça um programa que leia 10 números inteiros e escreva o menor valor
lido e o maior valor lido.
"""

maior = -999
menor = 999
for n in range(1, 6):
    valor = float(input('Digite um valor: '))
    if valor > 0:
        if valor > maior:
            maior = valor
    else:
        if valor < menor:
            menor = valor
        valor = float(input('Digite um valor: '))
print('Maior valor:', maior)
print('Menor valor:', menor)
