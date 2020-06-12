from time import sleep
print('-=-=-=-= DESAFIO 99 -=-=-=-=')
print()


def maior(* num):   # MINHA RESOLUÇÃO FOI COM TUPLA
    print('-='*20)
    print('Analisando os valores passados...')
    maior = 0
    for c, n in enumerate(num):   # TUPLA
        if c == 0 or n > maior:
            maior = n
        print(n, end=' ')
        sleep(0.5)
    print()
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


# RESOLUÇÃO do PROF:
# def maior(* num):
#     cont = maior = 0
#     for valor in num:
#         print(f'{valor} ', end='')
#         sleep(0.5)
#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
#         cont += 1
#     print(f'{cont} valores ao todx')
#     print(f'O maior foi {maior}')
