from random import choice
from time import sleep
import emoji
cores = {'azul':'\033[36m',
         'amarelo':'\033[33m',
         'roxo':'\033[35m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'limpa':'\033[m'}

print('-=-=-=-= DESAFIO 45 -=-=-=-=')
print()
print('{}{}{}'.format(cores['azul'], '-='*20, cores['limpa']))
print('{}{:^40}{}'.format(cores['amarelo'], 'JOKENPÔ', cores['limpa']))
print('{}{}{}'.format(cores['azul'], '-='*20, cores['limpa']))
print()

lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)

print('{}{}{}'.format(cores['roxo'], '[1] Pedra\n[2] Papel\n[3] Tesoura', cores['limpa']))
print()
us = int(input('Usuário: '))
print()

if us != 1 and us != 2 and us != 3:
    print('OPÇÃO INVÁLIDA! Tente novamente.')
elif us == 1 or us == 2 or us == 3:
    print(cores['amarelo'], 'JO', cores['limpa'])
    sleep(0.5)
    print(cores['amarelo'], 'KEN', cores['limpa'])
    sleep(0.5)
    print(cores['amarelo'], 'PÔ!!', cores['limpa'])
    print()
    print('Computador: {}'.format(pc))

if us == 1:
    if pc == 'Pedra':
        print('EMPATE!')
    elif pc == 'Tesoura':
        print(emoji.emojize('Você {}{}{}! :blush:', use_aliases=True).format(cores['verde'], 'GANHOU', cores['limpa']))
    elif pc == 'Papel':
        print(emoji.emojize('Você {}{}{}! :worried:', use_aliases=True).format(cores['vermelho'], 'PERDEU', cores['limpa']))
elif us == 2:
    if pc == 'Tesoura':
        print(emoji.emojize('Você {}{}{}! :worried:', use_aliases=True).format(cores['vermelho'], 'PERDEU', cores['limpa']))
    elif pc == 'Papel':
        print('EMPATE!')
    elif pc == 'Pedra':
        print(emoji.emojize('Você {}{}{}! :blush:', use_aliases=True).format(cores['verde'], 'GANHOU', cores['limpa']))
elif us == 3:
    if pc == 'Papel':
        print(emoji.emojize('Você {}{}{}! :blush:', use_aliases=True).format(cores['verde'], 'GANHOU', cores['limpa']))
    elif pc == 'Pedra':
        print(emoji.emojize('Você {}{}{}! :worried:', use_aliases=True).format(cores['vermelho'], 'PERDEU', cores['limpa']))
    elif pc == 'Tesoura':
        print('EMPATE!')
print('{}{}{}'.format(cores['azul'], '-='*20, cores['limpa']))
