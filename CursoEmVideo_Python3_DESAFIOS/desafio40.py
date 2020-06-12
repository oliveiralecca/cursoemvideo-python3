from time import sleep
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

print('-=-=-=-= DESAFIO 40 -=-=-=-=')
print()
print('{:=^40}'.format(' COLÉGIO OLIV '))
nome = str(input('Nome do aluno: ')).strip().title()
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print()
print('CALCULANDO...')
sleep(2)
print()
print('Média: {}{:.1f}{}'.format(cores['vermelho'], m, cores['limpa']))
if m < 5.0:
    print('O aluno {}{}{} está {}{}{}!'.format(cores['azul'], nome, cores['limpa'], cores['azul'], 'REPROVADO', cores['limpa']))
elif 5.0 <= m < 7.0:
    print('O aluno {}{}{} está em {}{}{}!'.format(cores['azul'], nome, cores['limpa'], cores['azul'], 'RECUPERAÇÃO', cores['limpa']))
else:
    print('O aluno {}{}{} está {}{}{}!'.format(cores['azul'], nome, cores['limpa'], cores['azul'], 'APROVADO', cores['limpa']))
print('='*40)
