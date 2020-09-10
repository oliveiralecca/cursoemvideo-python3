print('-=-=-=-= DESAFIO 91 -=-=-=-=')
print()

from random import randint
from time import sleep
from operator import itemgetter

jogos = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
         'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = []

print('VALORES SORTEADOS:')
sleep(1)
for k, v in jogos.items():
    print(f'    O {k} tirou {v}')
    sleep(1)
print()

print('== RANKING DOS JOGADORES ==')
sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
# SE itemgetter() FOSSE 0, O PARÂMETRO DE RANKEAR SERIA O NOME DOS JOGADORES
for c, v in enumerate(ranking):
    print(f'{c+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
