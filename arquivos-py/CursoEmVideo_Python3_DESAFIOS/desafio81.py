print('-=-=-=-= DESAFIO 81 -=-=-=-=')
print()

num = []
while True:
    num.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print(f'O número 5 faz parte da lista, e está nas posições ', end='')
    for i, n in enumerate(num):
        if n == 5:
            print(i, end='...')
else:
    print('O número 5 não foi encontrado na lista!')
print()
