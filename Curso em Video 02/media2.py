
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Aluno reprovado!'.upper())
elif media >= 5.0 and media <= 6.9:
    print('Aluno de recuperação!'.upper())
elif media >= 7.0:
    print('Aluno aprovado!'.upper())
