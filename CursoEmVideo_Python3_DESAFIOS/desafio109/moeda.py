def aumentar(n=0, pctg=0, formato=False):
    res = n + (n * pctg / 100)
    return res if formato is False else moeda(res)


def diminuir(n=0, pctg=0, formato=False):
    res = n - (n * pctg/100)
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)  # QUER DIZER A MESMA COISA QUE O RETURN ACIMA


def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
