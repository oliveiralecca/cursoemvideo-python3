from random import randint
from time import sleep
print('-=-=-=-= DESAFIO 100 -=-=-=-=')
print()


def sorteia(lista):
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(f'Sorteando 5 valores da lista: ', end='')
    for n in lista:
        print(n, end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    sPar = 0
    for n in lista:
        if n % 2 == 0:
            sPar += n
    print(f'Somando os valores pares de {lista}, temos {sPar}')


numeros = []
sorteia(numeros)
somaPar(numeros)
