cores = {'amarelo':'\033[33m',
         'azul':'\033[34m',
         'limpa':'\033[m'}

print('-=-=-=-= DESAFIO 38 -=-=-=-=')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
if n1 > n2:
    print('O {}{}{} é {}{}{}!'.format(cores['amarelo'], 'primeiro valor', cores['limpa'], cores['azul'], 'maior', cores['limpa']))
elif n2 > n1:
    print('O {}{}{} é {}{}{}!'.format(cores['amarelo'], 'segundo valor', cores['limpa'], cores['azul'], 'maior', cores['limpa']))
else:
    print('{}{}{} valor maior, os dois são {}{}{}!'.format(cores['amarelo'], 'Não existe', cores['limpa'], cores['azul'], 'iguais', cores['limpa']))
