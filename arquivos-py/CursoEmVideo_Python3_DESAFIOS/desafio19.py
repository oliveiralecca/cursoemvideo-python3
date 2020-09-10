from random import choice
print('======= DESAFIO 19 =======')
a1 = input('ALUNO 1: ')
a2 = input('ALUNO 2: ')
a3 = input('ALUNO 3: ')
a4 = input('ALUNO 4: ')
todos = [a1, a2, a3, a4]   # lista, é escrita dentro de []
escolhido = choice(todos)
print('O aluno escolhido foi {}!'.format(escolhido))
