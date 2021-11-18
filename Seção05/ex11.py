"""
Faça um programa que leia um número inteiro maior que 0 e devolva,
na tela, a soma de todos seus algarismos. Por exemplo, ao número 251
corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior que
0, o programa terminará com a mensagem: "Número inválido!".
"""

numero = int(input('Digite um número: '))

if numero < 1:
    print('Número inválido!')
else:
    soma = (numero[0:1] + numero[0:2] + numero[0:3])
    print('Soma dos algarismos:', soma)

# NÃO RESOLVIDO #
