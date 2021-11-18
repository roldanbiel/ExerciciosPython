
dist = float(input('Qual a distância da sua viagem? '))

if dist <= 200.0:
    preco = dist * 0.5
    print('Sua passagem irá custar R${}.'.format(preco))
else:
    preco = dist * 0.45
    print('Sua passagem irá custar R${}.'.format(preco))
