def dobra(lst):   # ALÉM DO DESEMPACOTAMENTO, OUTRA FORMA DE PASSAR VÁRIOS VALORES (COM LISTAS)
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# A PASSAGEM DE VALORES EM PYTHON É "POR REFERÊNCIA" E NÃO "POR VALOR",
# TUDO QUE FOR FEITO EM "LST", VAI INTERFERIR NA LISTA "VALORES".
