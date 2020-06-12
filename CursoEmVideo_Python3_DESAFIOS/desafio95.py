print('-=-=-=-=-= DESAFIO 95 -=-=-=-=')
print()

print('=-='*15)
print(f'{"APROVEITAMENTO DO JOGADOR":^45}')
print('=-='*15)

jogador = {}
time = []

while True:
    gols = []
    jogador['nome'] = str(input('Nome: ')).title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Gols na partida {c}: ')))
        jogador['gols'] = gols
        jogador['total'] = sum(gols)
    time.append(jogador.copy())
    continuar = ' '
    print('-'*45)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('=-='*15)
        break
    print('-'*45)

# TABELA
print(f'{"COD":5}', end='')
for k in jogador.keys():
    print(f'{k.upper():15}', end='')
print()
print('-'*41)
for i, j in enumerate(time):
    print(f'{i:<5}', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('-'*41)

while True:
    op = int(input('Mostrar dados de qual jogador? (999 para SAIR) '))
    if op == 999:
        break
    if op >= len(time):
        print(f'ERRO! Não existe jogador com código {op}. Tente novamente...')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[op]["nome"]}:')
        for c, gl in enumerate(time[op]['gols']):
            print(f'   Na partida {c+1}, fez {gl} gols.')
    print('-'*41)
print()
print('<< VOLTE SEMPRE! >>')
