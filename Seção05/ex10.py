"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule
e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde
a altura).

- Homens: (72 * h) - 58
- Mulheres: (62.1 * h) - 44.7
"""


peso_ideal = 0
sexo = str(input('Digite seu sexo (M ou F): '))
altura = float(input('Digite sua altura: '))

if sexo == 'M' or sexo == 'm':
    peso_ideal = (72 * altura) - 58
    print('Seu peso ideal é de:', peso_ideal, 'Kg.')
elif sexo == 'F' or sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print('Seu peso ideal é de:', peso_ideal, 'Kg')
else:
    print('Sexo inválido.')
