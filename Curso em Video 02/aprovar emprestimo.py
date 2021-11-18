
print('='*24)
print('Aprovador de empréstimos')
print('='*24)

valor = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))

prest = valor / (anos * 12)
excedente = salario * 0.3

print('Sua prestação é de R${:.2f}.'.format(int(prest)))
if prest <= excedente:
    print('Empréstimo não autorizado!'.upper())
else:
    print('Empréstimo autorizado!'.upper())
