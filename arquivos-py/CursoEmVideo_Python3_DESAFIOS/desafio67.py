print('-=-=-=-= DESAFIO 67 -=-=-=-=')
print()

print('{:=^50}'.format(' TABUADA '))
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 50)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont:2} = {n*cont}')
    print('-' * 50)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
