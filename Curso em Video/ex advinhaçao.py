import random

numero = random.randint(0, 5)

print('Tente advinhar em qual número eu pensei.')
adv = int(input('Qual número você acha que eu pensei? '))
if adv == numero:
    print('Parabéns, você acertou o número que eu pensei. Muito espertinho!')
else:
    print('Você não conseguiu advinhar o número que eu pensei. HAHAHA!')
