from datetime import date
from time import sleep
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}

print('-=-=-=-= DESAFIO 41 -=-=-=-=')
print()
print('{:=^50}'.format(' CONFEDERAÇÃO NACIONAL DE NATAÇÃO '))
nome = str(input('Nome do aluno: '))
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print()
print('PROCESSANDO...')
sleep(2)
print()
print('Idade: {}{}{} anos'.format(cores['amarelo'], idade, cores['limpa']))
if idade <= 9:
    print('Categoria: {}{}{}'.format(cores['azul'], 'MIRIM', cores['limpa']))
elif idade <= 14:
    print('Categoria: {}{}{}'.format(cores['azul'], 'INFANTIL', cores['limpa']))
elif idade <= 19:
    print('Categoria: {}{}{}'.format(cores['azul'], 'JUNIOR', cores['limpa']))
elif idade <= 25:
    print('Categoria: {}{}{}'.format(cores['azul'], 'SÊNIOR', cores['limpa']))
else:
    print('Categoria: {}{}{}'.format(cores['azul'], 'MASTER', cores['limpa']))
print('='*50)
