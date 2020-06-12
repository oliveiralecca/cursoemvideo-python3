def aumentar(n=0, pctg=0, formato=False):
    res = n + (n * pctg / 100)
    return res if formato is False else moeda(res)


def diminuir(n=0, pctg=0, formato=False):
    res = n - (n * pctg/100)
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, aum=10, red=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))   # CENTRALIZADO EM 40 ESPAÇOS
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')   # \t = 1 TABULAÇÃO, PARA ARRUMAR NA TABELA
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{red}% de redução: \t{diminuir(n, red, True)}')
    print('-'*30)
