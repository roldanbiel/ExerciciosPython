
algo = str(input('Digite algo: ')).upper().strip()

print('Você digitou: {}'.format(algo.capitalize()))
print('A letra A aparece {} vezes.'.format(algo.count('A')))
print('A primeira letra A aparece na posição {}.'.format(algo.find('A') + 1))
print('A última letra A aparece na posição {}.'.format(algo.rfind('A') + 1))
