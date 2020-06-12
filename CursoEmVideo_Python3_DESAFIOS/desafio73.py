print('-=-=-=-= DESAFIO 73 -=-=-=-=')
print()

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'Lista de times do Brasileirão 2019: {times}')
print('~'*35)
print(f'Os 5 primeiros são: {times[0:5]}')
print('~'*35)
print(f'Os 4 últimos são: {times[-4:]}')
print('~'*35)
print(f'Times em ordem alfabética: {sorted(times)}')
print('~'*35)
print('O Chapecoense está na {}ª posição'.format(times.index('Chapecoense')+1))
