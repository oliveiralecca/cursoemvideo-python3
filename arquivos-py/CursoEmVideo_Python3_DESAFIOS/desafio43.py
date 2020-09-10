from time import sleep
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[36m'}

print('-=-=-=-= DESAFIO 43 -=-=-=-=')
print()
print('{:=^35}'.format(' IMC '))
nome = str(input('Nome do paciente: '))
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura ** 2)
print()
print('CALCULANDO...')
sleep(1.5)
print()
print('IMC = {}{:.1f}{}'.format(cores['azul'], imc, cores['limpa']))
if imc < 18.5:
    print('{}{}{}'.format(cores['vermelho'], 'ABAIXO DO PESO', cores['limpa']))
elif 18.5 <= imc < 25:
    print('{}{}{}'.format(cores['verde'], 'PESO IDEAL', cores['limpa']))
elif 25 <= imc < 30:
    print('{}{}{}'.format(cores['amarelo'], 'SOBREPESO', cores['limpa']))
elif 30 <= imc < 40:
    print('{}{}{}'.format(cores['vermelho'], 'OBESIDADE', cores['limpa']))
else:
    print('{}{}{}'.format(cores['vermelho'], 'OBESIDADE MÓRBIDA', cores['limpa']))
print('='*35)
