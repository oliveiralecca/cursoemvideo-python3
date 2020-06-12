print('-=-=-=-= DESAFIO 42 -=-=-=-=')
print()
print('{:=^30}'.format(' TRIÂNGULOS '))
r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não é possível formar um triângulo com essas retas!')
print('='*30)
