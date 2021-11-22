soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c  # acumulador
        cont = cont + 1  # contador
print(soma)
print(cont)
