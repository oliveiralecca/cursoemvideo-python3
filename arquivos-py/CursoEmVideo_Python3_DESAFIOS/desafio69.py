print('-=-=-=-= DESAFIO 69 -=-=-=-=')
print()

pessoas = homens = mulheres = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    print('-'*30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print()
print('{:=^35}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas maiores de 18 anos: {pessoas}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
