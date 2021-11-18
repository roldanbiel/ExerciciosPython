from datetime import date

ano = date.today().year
idade = int(input('Ano de nascimento do atleta: '))
if idade > ano:
    print('Ano inválido.')
    idade = int(input('Ano de nascimento do atleta: '))
categoria = ano - idade
print('O atleta tem {} anos.'.format(categoria))
if categoria <= 9:
    print('Nadador de categoria MIRIM.')
elif categoria <= 14:
    print('Nadador de categoria INFANTIL.')
elif categoria <= 19:
    print('Nadador de categoria JUNIOR.')
elif categoria <= 25:
    print('Nadador de categoria SÊNIOR.')
else:
    print('Nadador de categoria MASTER.')
