print('-=-=-=-= DESAFIO 72 -=-=-=-=')
print()

num = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze',
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    resp = int(input('Digite um número entre 0 e 20: '))
    while resp not in range(0, 21):
        resp = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    resp = num[resp]
    print(f'Você digitou o número {resp}')
    print('='*25)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('=' * 25)
    if continuar == 'N':
        break

# RESOLUÇÃO do PROF:
# while True:
#     resp = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= resp <= 20:
#         break
#     print('Tente novamente. ', end='')
# print(f'Você digitou o número {num[resp]}')
