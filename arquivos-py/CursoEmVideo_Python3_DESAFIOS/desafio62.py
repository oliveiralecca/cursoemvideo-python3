print('-=-=-=-= DESAFIO 62 -=-=-=-=')
print()
print('{:=^50}'.format(' PA '))
termo = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
c = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while c < total:
        print(termo, end=' → ')
        termo += raz
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print()
print('PA finalizada com {} termos mostrados.'.format(total))
