
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))

valor_dia = dias * 60
valor_km = km * 0.15
total = valor_km + valor_dia

print('Total a pagar pelo aluguel R${}.'.format(total))
