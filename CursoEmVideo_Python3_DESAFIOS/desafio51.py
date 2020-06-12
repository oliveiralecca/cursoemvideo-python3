print('-=-=-=-= DESAFIO 51 -=-=-=-=')
print()
print('{:=^25}'.format(' PA '))
termo = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
num = termo + (11 - 1) * raz   # FÓRMULA MATEMÁTICA DO N TERMO DE UMA PA
for c in range(termo, num, raz):
    print(c, end=' > ')
print('ACABOU!')
print('='*25)
