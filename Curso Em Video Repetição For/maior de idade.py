from datetime import date

ano = date.today().year
soma = 0
soma1 = 0
for c in range(1, 8):
    nascimento = int(input('Informe sua data de nascimento: '))
    maior = ano - nascimento
    if maior >= 18:
        soma = soma + 1
    else:
        soma1 = soma1 + 1
print('{} pessoas são maiores de idade.'.format(soma))
print('{} pessoas não são maiores de idade.'.format(soma1))
