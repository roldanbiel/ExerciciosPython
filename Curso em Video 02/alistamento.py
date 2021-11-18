from datetime import date

nascimento = int(input('Informe seu ano de nascimento: '))

ano = date.today().year
diff = (ano - nascimento) - 18
if diff < 0:
    diff = diff * -1

if ano - nascimento <= 17:
    print('Calma, jovem. Ainda não chegou sua hora de se alistar!')
    print('Faltam ainda {} anos.'.format(diff))
elif ano - nascimento == 18:
    print('Chegou sua hora de se alistar para o exército. Boa sorte!')
elif ano - nascimento > 18:
    print('Já passou da sua hora de se alistar. Entre no site e faça o procedimento.')
    print('Já se passaram {} anos.'.format(diff))
