from random import randint
from time import sleep
print('-=-=-=-= DESAFIO 88 -=-=-=-=')
print()

print('-'*35)
print(f'{"JOGA NA MEGA SENA":^35}')
print('-'*35)

n = int(input('Quantos jogos você quer que eu sorteie? '))
print()

lista = []
jogos = []
tot = 1
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('=-='*3, f'{"SORTEANDO"} {n} {"JOGOS"}', '=-='*3)
for c, l in enumerate(jogos):
    print(f'Jogo {c+1}: {l}')
    sleep(1)
print('=-='*4, f'{"< BOA SORTE! >"}', '=-='*4)
