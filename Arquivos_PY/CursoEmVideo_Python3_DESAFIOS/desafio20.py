from random import shuffle
print('======= DESAFIO 20 =======')
a1 = input('ALUNO 1: ')
a2 = input('ALUNO 2: ')
a3 = input('ALUNO 3: ')
a4 = input('ALUNO 4: ')
todos = [a1, a2, a3, a4]
shuffle(todos)
print('A ordem de apresentação dos trabalhos será:\n {}'.format(todos))
