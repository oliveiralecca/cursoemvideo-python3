estado = {}   # OU: estado = dict()
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())   # O MÉTODO .COPY() É O MESMO QUE O FATIAMENTO [:] DAS LISTAS

for e in brasil:   # LAÇO PARA A LISTA
    for v in e.values():   # LAÇO PARA OS DICIONÁRIOS
        print(v, end=' ')
    print()

# for k, v in e.items():   # CADA ESTADO É UM DICIONÁRIO, POR ISSO .ITEMS()
    # print(f'A chave {k} tem valor {v}.')

# for e in brasil:
    # print(e['uf'])   # MOSTRA SÓ OS NOMES DOS ESTADOS






