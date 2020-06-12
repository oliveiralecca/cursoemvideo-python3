print('-=-=-=-= DESAFIO 78 -=-=-=-=')
print()

valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-='*15)
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(i, end='...')
print()

print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(i, end='...')
print()

# RESOLUÇÃO do PROF:
# valores = []
# mai = men = 0
# for c in range(0, 5):
#     valores.append(int(input(f'Digite um valor para a posição {c}: ')))
#     if c == 0:
#         mai = men = valores[c]
#     else:
#         if valores[c] > mai:
#             mai = valores[c]
#         if valores[c] < men:
#             men = valores[c]
