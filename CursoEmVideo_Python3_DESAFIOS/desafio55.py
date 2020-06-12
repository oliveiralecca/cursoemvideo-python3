print('-=-=-=-= DESAFIO 55 -=-=-=-=')
print()
print('{:=^45}'.format(' MAIOR E MENOR PESO '))
maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Peso da {}ª pessoa (kg): '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print()
print('O maior peso é {}{}{} kg e o menor é {}{}{} kg.'.format('\033[31m', maior, '\033[m', '\033[32m', menor, '\033[m'))
print('='*45)
