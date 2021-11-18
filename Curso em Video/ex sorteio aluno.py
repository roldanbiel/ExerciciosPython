from random import choice

aluno = input('Nome do aluno: ')
aluno1 = input('Nome do aluno: ')
aluno2 = input('Nome do aluno: ')
aluno3 = input('Nome do aluno: ')

lista = [aluno, aluno1, aluno2, aluno3]
escolhido = choice(lista)

print('O aluno escolhido foi {}.'.format(escolhido))
