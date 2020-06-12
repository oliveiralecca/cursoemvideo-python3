import emoji
from time import sleep
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m'}

print('-=-=-=-= DESAFIO 36 -=-=-=-=')
print()
print('{:=^50}'.format(' EMPRÉSTIMO BANCÁRIO '))
nome = str(input('Nome do requerente: ')).title().strip()
print(emoji.emojize('Olá, Sr(a) {}{}{}! Seja bem-vindo(a) ao nosso app :blush:', use_aliases=True).format(cores['azul'], nome, cores['limpa']))
print()
print('Vamos começar a simulação do seu empréstimo...')
sleep(4)
print()
casa = float(input('Valor do imóvel: R$'))
sal = float(input('Seu salário: R$'))
anos = float(input('Em quantos anos deseja pagar: '))
mensal = casa / (anos * 12)
print()
print('A prestação mensal ficou de R${}{:.2f}{}'.format(cores['amarelo'], mensal, cores['limpa']))
if mensal > (sal * 30/100):
    print('E esse valor ultrapassa 30% do seu salário.')
    print('Que pena, seu empréstimo foi {}{}{}!'.format(cores['vermelho'], 'NEGADO', cores['limpa']))
else:
    print('Parabéns! Seu empréstimo foi {}{}{}!'.format(cores['verde'], 'APROVADO', cores['limpa']))
print()
print(emoji.emojize('Obrigado por usar o nosso simulador! :blush:', use_aliases=True))
print('='*50)
