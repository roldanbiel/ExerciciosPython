
print('\033[1;33m-=-\033[m'*12)
print('\033[1;33m      Analisador de Triângulos      \033[m')
print('\033[1;33m-=-\033[m'*12)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('\033[1;32mOs segmentos podem formar um triângulo e esse triângulo é EQUILÁTERO.\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;32mOs segmentos podem formar um triângulo e esse triângulo é ESCALENO.\033[m')
    else:
        print('\033[1;32mOs segmentos podem formar um triângulo e esse triângulo é ISÓSCELES.\033[m')
else:
    print('\033[1;31mOs segmentos não podem formar um triângulo.\033[m')
