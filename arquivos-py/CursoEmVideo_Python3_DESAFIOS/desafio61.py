print('-=-=-=-=DESAFIO 61 -=-=-=-=')
print()
print('{:=^50}'.format(' PA '))
termo = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
c = 0
while c < 10:
    print(termo, end=' → ')
    termo += raz
    c += 1
print('FIM')
print('='*50)
