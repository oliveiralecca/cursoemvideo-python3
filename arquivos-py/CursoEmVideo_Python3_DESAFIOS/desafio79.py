print('-=-=-=-= DESAFIO 79 -=-=-=-=')
print()

num = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=-='*15)
num.sort()
print(f'Você digitou os valores {num}')
