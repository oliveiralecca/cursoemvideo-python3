print('-=-=-=-= DESAFIO 28 -=-=-=-=')
print()
from random import randint
from time import sleep
print('{:=^35}'.format(' JOGO DA ADIVINHAÇÃO '))
num_pc = randint(0, 5)
num_us = int(input('Adivinhe o número escolhido por mim (0-5): '))
print('PROCESSANDO...')
sleep(3)
if num_us == num_pc:
    print('Parabéns!\nVocê VENCEU \o/')
else:
    print('Que pena!\nVocê ERROU :/\nEu pensei no número {}.'.format(num_pc))
print('=' * 35)
