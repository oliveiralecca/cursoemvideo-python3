print('-=-=-=-= DESAFIO 50 -=-=-=-=')
print()
print('{:=^30}'.format(' SOMA DOS PARES '))
s = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        s += num
print()
print('A soma dos PARES vale {}'.format(s))
print('='*30)
