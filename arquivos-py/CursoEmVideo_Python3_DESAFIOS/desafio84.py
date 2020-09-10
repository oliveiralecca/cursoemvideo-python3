print('-=-=-=-= DESAFIO 84 -=-=-=-=')
print()

pessoas = []
dados = []
pesadas = []
leves = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    print('=-='*10)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('=-='*10)
    if continuar == 'N':
        break

for c, p in enumerate(pessoas):
    if c == 0:
        maior = menor = p[1]
    elif p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]

for p in pessoas:
    if maior in p:
        pesadas.append(p[0])
    elif menor in p:
        leves.append(p[0])

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pesadas:
    print(f'[{p}]', end=' ')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in leves:
    print(f'[{p}]', end=' ')


# RESOLUÇÃO do PROF:
# while True:
#     dados.append(str(input('Nome: ')))
#     dados.append(float(input('Peso: ')))
#     if len(pessoas) == 0:
#        maior = menor = dados[1]
#     else:
#         if dados[1] > maior:
#             maior = dados[1]
#         if dados[1] < menor:
#             menor = dados[1]
#     pessoas.append(dados[:])
#     dados.clear()
# [. . .]
# for p in pessoas:
#     if p[1] == maior:
#         print(f'[{p[0]}]', end='')
# for p in pessoas:
#     if p[1] == menor:
#         print(f'[{p[0]}]', end='')
