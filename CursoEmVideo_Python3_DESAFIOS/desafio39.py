from datetime import date
from time import sleep
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azul':'\033[36m'}

print('-=-=-=-= DESAFIO 39 -=-=-=-=')
print()
print('{:=^50}'.format(' ALISTAMENTO MILITAR '))
nome = str(input('Nome: ')).title().strip()
print('''SEXO
 [1] Masculino
 [2] Feminino''')
op = int(input('OPÇÃO: '))
if op == 1:
    nasc = int(input('Ano de nascimento: '))
    print()
    ano = date.today().year
    idade = ano - nasc
    print('PROCESSANDO...')
    sleep(3)
    print()
    if idade < 18:
        tempo = 18 - idade
        print('{}, você {}{}{} ao serviço militar!'.format(nome, cores['amarelo'], 'ainda vai se alistar', cores['limpa']))
        print('Faltam {}{}{} anos.'.format(cores['azul'], tempo, cores['limpa']))
    elif idade == 18:
        print('{}, está na {}{}{}!'.format(nome, cores['amarelo'], 'hora de se alistar', cores['limpa']))
    elif idade > 18:
        tempo = idade - 18
        print('{}, já {}{}{} do alistamento!'.format(nome, cores['amarelo'], 'passou do tempo', cores['limpa']))
        print('Passaram-se {}{}{} anos.'.format(cores['azul'], tempo, cores['limpa']))
elif op == 2:
    print('Você não precisa fazer alistamento militar obrigatório!')
else:
    print('Comando inválido! Tente novamente.')
print('='*50)
