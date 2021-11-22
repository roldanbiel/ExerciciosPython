soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('Digite o {}° valor: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Foram informados {} valores pares e a soma deles é de {}.'.format(cont, soma))
