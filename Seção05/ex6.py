"""
Escreva um programa que, dado dois números inteiros, mostre na tela
o maior deles, assim como a diferença existente entre ambos.
"""

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > numero2:
    dif = numero1 - numero2
    print(numero1, 'é maior que', numero2)
    print('E a diferença entre eles é de:', dif)
elif numero1 == numero2:
    print('Números iguais.')
else:
    dif = numero2 - numero1
    print(numero2, 'é maior que', numero1)
    print('E a diferença entre eles é', dif)
