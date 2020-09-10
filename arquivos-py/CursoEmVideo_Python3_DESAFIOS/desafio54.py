from datetime import date
print('-=-=-=-= DESAFIO 54 -=-=-=-=')
print()
print('{:=^30}'.format(' MAIORIDADE '))
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Ano da pessoa {}: '.format(c)))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print()
print(' Menores de idade: {}\n Maiores de idade: {}'.format(menor, maior))
print('='*30)
