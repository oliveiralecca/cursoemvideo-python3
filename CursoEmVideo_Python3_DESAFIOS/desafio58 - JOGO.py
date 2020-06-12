from random import randint
cores = {'amarelo':'\033[33m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'limpa':'\033[m'}

print('-=-=-=-= DESAFIO 58 -=-=-=-=')
print()
print('{:=^53}'.format(' \033[33mJOGO DA ADIVINHAÇÃO v2.0\033[m '))
print('{}{}{}'.format(cores['azul'], '~'*41, cores['limpa']))
print('{}{}{}'.format(cores['vermelho'], 'Vou pensar em um número, tente adivinhar!', cores['limpa']))
print('{}{}{}'.format(cores['azul'], '~'*41, cores['limpa']))
pc = randint(0, 10)
jogador = ''
tentativas = 0
while jogador != pc:
    jogador = int(input('Em que número entre 0-10 eu pensei? '))
    tentativas += 1
    if jogador != pc:
        if jogador < pc:
            print('Mais...')
        else:
            print('Menos...')
print()
print('Correto! Pensei no número {}{}{}.'.format(cores['amarelo'], pc, cores['limpa']))
print('Você precisou de {}{} tentativas{} para acertar!'.format(cores['vermelho'], tentativas, cores['limpa']))
print('='*45)

# RESOLUÇÃO do PROF:
# acertou = False
# palpites = 0
# while not acertou:
#     jogador = int(input('Qual é seu palpite? '))
#     palpites += 1
#     if jogador == pc:
#         acertou = True
#     else:
#         if jogador < pc:
#             print('Mais...')
#         else:
#             print('Menos...')
# print('Acertou com {} tentativas!'.format(palpites))
