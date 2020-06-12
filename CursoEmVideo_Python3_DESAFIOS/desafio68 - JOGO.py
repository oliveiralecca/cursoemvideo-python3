from random import randint
from time import sleep
cores = {'azul': '\033[36m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'limpa': '\033[m'}

print('-=-=-=-= DESAFIO 68 -=-=-=-=')
print()

print('{}{}{}'.format(cores['azul'], '=-='*17, cores['limpa']))
print('{}{}{}'.format(cores['amarelo'], '              VAMOS JOGAR PAR OU ÍMPAR', cores['limpa']))
print('{}{}{}'.format(cores['azul'], '=-='*17, cores['limpa']))

venceu = perdeu = 0
while True:
    pc = randint(0, 10)
    valor = int(input('Diga um valor: '))
    parimpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*51)
    tot = valor + pc
    if parimpar == 'P':
        if tot % 2 == 0:
            print('Você jogou {} e o computador {}. Total de {} deu {}{}{}'.format(valor, pc, tot, cores['azul'], 'PAR', cores['limpa']))
            print('-'*51)
            print('Você {}{}{}!\nVamos jogar novamente...'.format(cores['vermelho'], 'VENCEU', cores['limpa']))
            print('{}{}{}'.format(cores['azul'], '=-='*17, cores['limpa']))
            venceu += 1
            sleep(2)
        else:
            print('Você jogou {} e o computador {}. Total de {} deu {}{}{}'.format(valor, pc, tot, cores['azul'], 'ÍMPAR', cores['limpa']))
            print('-'*51)
            print('Você {}{}{}!'.format(cores['vermelho'], 'PERDEU', cores['limpa']))
            print('{}{}{}'.format(cores['azul'], '=-='*17, cores['limpa']))
            print('\033[33mGAME OVER!\033[m', end=' ')
            perdeu += 1
    elif parimpar == 'I':
        if tot % 2 == 1:
            print('Você jogou {} e o computador {}. Total de {} deu {}{}{}'.format(valor, pc, tot, cores['azul'], 'ÍMPAR', cores['limpa']))
            print('-'*51)
            print('Você {}{}{}!\nVamos jogar novamente...'.format(cores['vermelho'], 'VENCEU', cores['limpa']))
            print('{}{}{}'.format(cores['azul'], '=-='*17, cores['limpa']))
            venceu += 1
            sleep(2)
        else:
            print('Você jogou {} e o computador {}. Total de {} deu {}{}{}'.format(valor, pc, tot, cores['azul'], 'PAR', cores['limpa']))
            print('-'*51)
            print('Você {}{}{}!'.format(cores['vermelho'], 'PERDEU', cores['limpa']))
            print('{}{}{}'.format(cores['azul'], '=-='*17, cores['limpa']))
            print('\033[33mGAME OVER!\033[m', end=' ')
            perdeu += 1
    else:
        print('\033[33mComando inválido! Tente novamente.\033[m')
        print('{}{}{}'.format(cores['azul'], '=-='*17, cores['limpa']))
        sleep(2)
    if perdeu == 1:
        break
print(f'Você venceu {venceu} vezes.')
