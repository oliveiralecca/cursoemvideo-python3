print('-=-=-=-= DESAFIO 102 -=-=-=-=')
print()


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: Número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: Fatorial do número n
    """
    print('-'*30)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:  # ou seja, se show for VERDADEIRO
            if c > 1:
                print(c, end=' x ')
            else:
                print(f'{c} = ', end='')
    if not show:
        print(f'O fatorial de {n} é igual a ', end='')
    return f


print(fatorial(5, show=False))
# help(fatorial)   # MOSTRA O MANUAL, COMO USA A FUNÇÃO
