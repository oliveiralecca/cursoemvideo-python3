print('-=-=-=-= DESAFIO 60 -=-=-=-=')
print()
print('{:=^35}'.format(' FATORIAL '))
n = int(input('Digite um número: '))
cont = n
fat = 1
print('{}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))
print('='*35)

# for c in range(n, 0, -1):
#    fat = fat * c
# print('O fatorial de {} é igual a {}'.format(n, fat))

# RESOLUÇÃO do PROF:
# from math import factorial
# n = int(input('Digite um número: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))
