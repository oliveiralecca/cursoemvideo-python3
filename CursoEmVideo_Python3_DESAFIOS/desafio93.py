print('-=-=-=-= DESAFIO 93 -=-=-=-=')
print()

print('=-='*15)
print(f'{"APROVEITAMENTO DO JOGADOR":^45}')
print('=-='*15)

jogador = {}
gols = []

jogador['nome'] = str(input('Nome: ')).title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, partidas+1):
    gols.append(int(input(f'Gols na partida {c}: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-'*45)

print(jogador)
print('-'*45)

for k, v in jogador.items():
    print(f'{k.title()} = {v}')
print('-'*45)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, gl in enumerate(gols):
    print(f'    => Na partida {i+1}, fez {gl} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
