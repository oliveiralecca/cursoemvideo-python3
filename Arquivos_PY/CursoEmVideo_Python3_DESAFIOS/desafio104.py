print('-=-=-=-= DESAFIO 104 -=-=-=-=')
print()


def leiaInt(msg):
    print('-'*45)
    inteiro = str(input(msg))
    while not inteiro.isnumeric():
        print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
        inteiro = str(input(msg))
        if inteiro.isnumeric():
            break
    return inteiro


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
print('-'*45)


# RESOLUÇÃO do PROF:
# def leiaInt(msg):
    # ok = False
    # valor = 0
    # while True:
        # num = str(input(msg))
        # if num.isnumeric():
            # valor = int(num)
            # ok = True
        # else:
            # print('ERRO! Digite um número inteiro válido.')
        # if ok:
            # break
    # return valor
