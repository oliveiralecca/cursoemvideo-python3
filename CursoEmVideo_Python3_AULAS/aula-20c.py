def contador(* num):
    # print(num)   ELE CRIA UMA TUPLA COM OS VALORES PASSADOS, ENTÃO POSSO FAZER TUDO QUE FAÇO COM UMA TUPLA
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 6, 2)
