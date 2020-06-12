print('-=-=-=-= DESAFIO 82 -=-=-=-=')
print()

num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número inteiro: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('-='*25)
num.sort()
par.sort()
impar.sort()
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
