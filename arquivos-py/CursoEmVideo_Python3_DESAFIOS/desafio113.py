def leiaInt(msg):
    valido = False
    inteiro = int(input(msg))
    while valido:
        inteiro = int(input(msg))
        if int(inteiro):
            valido = True
    return inteiro


def leiaFloat(msg):
    valido = False
    real = float(input(msg))
    while valido:
        real = float(input(msg))
        if float(real):
            valido = True
    return real


# PROGRAMA PRINCIPAL
print('-'*50)
while True:
    try:
        n = leiaInt('Digite um número Inteiro: ')
    except KeyboardInterrupt:
        print('\033[31mUsuário preferiu não digitar esse número.\033[m')
        n = 0
        break
    except:
        print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
    else:
        break
while True:
    try:
        r = leiaFloat('Digite um número Real: ')
    except KeyboardInterrupt:
        print('\033[31mUsuário preferiu não digitar esse número.\033[m')
        r = 0
        print(f'O valor inteiro digitado foi {n} e o real foi {r}')
        break
    except:
        print('\033[31mERRO: por favor, digite um número real válido.\033[m')
    else:
        print(f'O valor inteiro digitado foi {n} e o real foi {r}')
        break
print('-'*50)


# RESOLUÇÃO do PROF:
# def leiaInt(msg):
    # while True:
        # try:
            # n = int(input(msg))
        # except (ValueError, TypeError):
            # print('ERRO: por favor, digite um número inteiro válido.')
            # continue   # VOLTA PARA O WHILE
        # except KeyboardInterrupt:
            # print('Entrada de dados interrompida pelo usuário.')
            # return 0
        # else:
            # return n


# def leiaFloat(msg):
    # while True:
        # try:
            # n = float(input(msg))
        # except(ValueError, TypeError):
            # print('ERRO: por favor, digite um número real válido.')
            # continue
        # except KeyboardInterrupt:
            # print('Entrada de dados interrompida pelo usuário.')
            # return 0
        # else:
            # return n


# n1 = leiaInt('Digite um Inteiro: ')
# n2 = leiaFloat('Digite um Real: ')
# print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
