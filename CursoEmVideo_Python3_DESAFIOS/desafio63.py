print('-=-=-=-= DESAFIO -=-=-=-=')
print()
print('{:=^40}'.format(' FIBONACCI '))
num = int(input('Quantos termos quer mostrar: '))
v1 = 0
print(v1, end=' → ')
v2 = 1
print(v2, end=' → ')
cont = 3
while cont < num+1:
    v3 = v1 + v2
    print(v3, end=' → ')
    v1 = v2
    v2 = v3
    cont += 1
print('FIM')
print('='*40)
