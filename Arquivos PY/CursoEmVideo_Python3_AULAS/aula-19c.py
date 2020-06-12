pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

for k in pessoas.keys():   #MOSTRA SÓ O NOME DAS CHAVES
    print(k)

print()

for v in pessoas.values():
    print(v)

print()

for k, v in pessoas.items():   # SUBSTITUI O "ENUMERATE" DAS TUPLAS E LISTAS
    print(f'{k} = {v}')

