def leiaDinheiro(msg):
    valido = False
    while not valido:
        ler = str(input(msg)).replace(',', '.').strip()
        if ler.isalpha() or ler == '':
            print(f'\033[31mERRO: "{ler}" não é um preço inválido!\033[m')
        else:
            valido = True
            return float(ler)
