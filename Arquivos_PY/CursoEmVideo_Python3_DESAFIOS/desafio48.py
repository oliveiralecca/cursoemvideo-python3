print('-=-=-=-= DESAFIO 48 -=-=-=-=')
print()
print('='*46)
print(' SOMA ENTRE ÍMPARES MÚLTIPLOS DE 3 ENTRE 1-500')
print('='*46)
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c   # ACUMULADOR
        cont += 1  # CONTADOR
print('Essa soma de todos os {} valores é {}'.format(cont, s))
