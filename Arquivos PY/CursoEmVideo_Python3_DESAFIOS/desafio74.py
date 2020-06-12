from random import randint
print('-=-=-=-= DESAFIO 74 -=-=-=-=')
print()

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10))
print('Os números sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
print()
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
