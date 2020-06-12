print('-=-=-=-= DESAFIO 103 -=-=-=-=')
print()


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    print('-'*50)


print('-'*50)
n = str(input('Nome do Jogador: ')).strip().title()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
