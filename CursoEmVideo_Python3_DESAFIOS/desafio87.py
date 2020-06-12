print('-=-=-=-= DESAFIO 87 -=-=-=-=')
print()

matriz = [[], [], []]
somapar = soma3col = maior = 0

# PRIMEIRA LINHA
for a in range(0, 3):
    n = int(input(f'Digite um número para [{0}, {a}]: '))
    matriz[0].append(n)
    if n % 2 == 0:
        somapar += n
    if a == 2:
        soma3col += n

# SEGUNDA LINHA
for b in range(0, 3):
    n = int(input(f'Digite um número para [{1}, {b}]: '))
    matriz[1].append(n)
    if n % 2 == 0:
        somapar += n
    if b == 2:
        soma3col += n
    if b == 0 or n > maior:
        maior = n

# TERCEIRA LINHA
for c in range(0, 3):
    n = int(input(f'Digite um número para [{2}, {c}]: '))
    matriz[2].append(n)
    if n % 2 == 0:
        somapar += n
    if c == 2:
        soma3col += n

print('=-='*15)
for m in matriz[0]:
    print(f'[ {m:^5} ]', end=' ')
print()
for m in matriz[1]:
    print(f'[ {m:^5} ]', end=' ')
print()
for m in matriz[2]:
    print(f'[ {m:^5} ]', end=' ')
print()
print('=-='*15)

print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {soma3col}.')
print(f'O maior valor da segunda linha é {maior}.')


# RESOLUÇÃO do PROF:
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-='*30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#         if matriz[l][c] % 2 == 0:
#             somapar += matriz[l][c]
#     print()
# print('-='*30)
# for l in range(0, 3):
#     soma3col += matriz[l][2]
# for c in range(0, 3):
#     if c == 0 or matriz[1][c] > maior:
#         maior = matriz[1][c]