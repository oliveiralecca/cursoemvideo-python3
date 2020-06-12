print('-=-=-=-= DESAFIO 56 -=-=-=-=')
print()
print('{:=^45}'.format(' ANALISADOR DE PESSOAS '))
sid = 0
m = 0
velho = 0
nome2 = ''
mulher = 0
for c in range(1, 5):
    print('{:^14}{}'.format('PESSOA', c))
    print('------------------')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    print('------------------')
    sid += idade
    m = sid / 4
    if sexo == 'M':
        if idade > velho:
            velho = idade
            nome2 = nome
    if sexo == 'F':
        if idade < 20:
           mulher += 1
print()
print('A média das idades é {:.1f}'.format(m))
print('O homem mais velho tem {} anos e é {}'.format(velho, nome2))
print('{} mulheres têm menos de 20 anos'.format(mulher))
print('='*45)
