print('-=-=-=-= DESAFIO 92 -=-=-=-=')
print()

from datetime import date

print('=-='*15)
print(f'{"FICHA DO TRABALHADOR":^45}')
print('=-='*15)

trabalhador = {}

while True:
    trabalhador['nome'] = str(input('Nome: ')).title()
    nasc = int(input('Ano de Nascimento: '))
    atual = date.today().year
    trabalhador['idade'] = atual - nasc
    trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if trabalhador['ctps'] == 0:
        break
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = 35 - (atual - trabalhador['contratação']) + trabalhador['idade']
    if trabalhador['salário'] != 0:
        break
print('-'*45)
for k, v in trabalhador.items():
    print(f'{k.title()} = {v}')


# RESOLUÇÃO do PROF:
# if trabalhador['ctps'] != 0:
#     trabalhador['contratação'] = ...
#     trabalhador['salário'] = ...
#     trabalhador['aposentadoria'] = ...
