print('-=-=-=-= DESAFIO 49 -=-=-=-=')
print()
print('{:=^25}'.format(' TABUADA '))
num = int(input('Escolha um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('='*25)
