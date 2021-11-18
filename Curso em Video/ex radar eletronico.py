
velo = float(input('Velocidade: '))

if velo > 80.0:
    diff = velo - 80
    multa = diff * 7
    print('Você ultrapassou o limite de velocidade, então uma multa será aplicada.')
    print('Sua multa foi de R${}.'.format(multa))
