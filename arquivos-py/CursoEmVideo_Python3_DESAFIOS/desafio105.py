print('-=-=-=-= DESAFIO 105 -=-=-=-=')
print()


def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a turma
    """
    print('-'*75)
    resumo = {}
    totnum = maior = menor = soma = 0
    for c, n in enumerate(num):
        totnum += 1
        soma += n
        resumo['total'] = totnum
        if c == 0:
            maior = menor = n
            resumo['maior'] = n
            resumo['menor'] = n
        else:
            if n > maior:
                maior = n
                resumo['maior'] = maior
            elif n < menor:
                menor = n
                resumo['menor'] = menor
        resumo['média'] = soma / totnum
    if sit:
        if resumo['média'] >= 7:
            resumo['situação'] = 'BOA'
        elif resumo['média'] < 5:
            resumo['situação'] = 'RUIM'
        else:
            resumo['situação'] = 'RAZOÁVEL'
    return resumo


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
# help(notas)


# RESOLUÇÃO do PROF:
# def notas(* n, sit=False):
    # r = dict()
    # r['total'] = len(n)
    # r['maior'] = max(n)
    # r['menor'] = min(n)
    # r['média'] = sum(n)/len(n)
    # if sit:
        # if r['média'] >= 7:
            # r['situação'] = 'BOA'
        # elif r['média'] >= 5:
            # r['situação'] = 'RAZOÁVEL'
        # else:
            # r['situação'] = 'RUIM'
    # return r
