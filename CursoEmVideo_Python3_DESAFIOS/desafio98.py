from time import sleep
print('-=-=-=-= DESAFIO 98 -=-=-=-=')
print()


def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.5)
        print()
        print('Contagem finalizada!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.5)
        print()
        print('Contagem finalizada!')


contador(1, 10, 1)
contador(10, 0, 2)

print('=-'*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
