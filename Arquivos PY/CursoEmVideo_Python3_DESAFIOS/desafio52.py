print('-=-=-=-= DESAFIO 52 -=-=-=-=')
print()
num = int(input('Digite um número: '))
divisores = 0
for c in range(1, num+1):
    if num % c == 0:
        print('{}{}{}'.format('\033[32m', c, '\033[m'), end=' ')
        divisores += 1
    else:
        print('{}{}{}'.format('\033[31m', c, '\033[m'), end=' ')
if divisores == 2:
    print()
    print('O número {} É PRIMO!'.format(num))
else:
    print()
    print('O número {} NÃO É PRIMO!'.format(num))
