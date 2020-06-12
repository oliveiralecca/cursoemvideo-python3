print('-=-=-=-= DESAFIO 59 -=-=-=-=')
print()
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
op = 0
while op != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    op = int(input('OPÇÃO: '))
    if op == 1:
        print('A soma entre {} + {} vale {}!'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação entre {} x {} vale {}!'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é {}!'.format(n1, n2, n1))
        else:
            print('O maior número entre {} e {} é {}!'.format(n1, n2, n2))
    elif op == 4:
        print('Digite os novos números:')
        n1 = int(input('1º número: '))
        n2 = int(input('2º número: '))
    else:
        if op != 5:
            print('Opção inválida! Tente novamente.')
    print('-='*14)
