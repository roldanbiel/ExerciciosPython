import random
import time

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''ESCOLHA:
  [0] - PEDRA
  [1] - PAPEL
  [2] - TESOURA''')

jogador = int(input('Escolha o que você vai jogar: '))
time.sleep(0.5)
print('JO')
time.sleep(0.8)
print('KEN')
time.sleep(0.8)
print('PO!!!')
print('-='*11)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-='*11)

if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
if computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
if computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INVÁLIDA')
