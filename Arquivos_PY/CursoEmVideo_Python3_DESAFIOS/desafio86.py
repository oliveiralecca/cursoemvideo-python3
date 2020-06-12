print('-=-=-=-= DESAFIO 86 -=-=-=-=')
print()

matriz = [[], [], []]

for a in range(0, 3):
    n = int(input(f'Digite um número para [{0}, {a}]: '))
    matriz[0].append(n)
for b in range(0, 3):
    n = int(input(f'Digite um número para [{1}, {b}]: '))
    matriz[1].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um número para [{2}, {c}]: '))
    matriz[2].append(n)

print('=-='*15)
for m in matriz[0]:
    print(f'[ {m:^3} ]', end=' ')
print()
for m in matriz[1]:
    print(f'[ {m:^5} ]', end=' ')
print()
for m in matriz[2]:
    print(f'[ {m:^5} ]', end=' ')


# RESOLUÇÃO do PROF:
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
#     print('-='*30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()
