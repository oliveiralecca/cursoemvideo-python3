# CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)   # MOSTRA UMA LISTA COM 2 DICIONÁRIOS DENTRO
print(brasil[0])   # MOSTRA O DICIONÁRIO DO RJ
print(brasil[1]['uf'])   # MOSTRA "SÃO PAULO"
print(brasil[0]['sigla'])   # MOSTRA "RJ"
