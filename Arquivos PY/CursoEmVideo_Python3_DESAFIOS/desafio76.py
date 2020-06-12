print('-=-=-=-= DESAFIO 76 -=-=-=-=')
print()

print('-'*45)
print('{:^45}'.format('LISTAGEM DE PREÇOS'))
print('-'*45)

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
            'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for cont in range(0, len(produtos)):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<34}', end='')
    else:
        print(f'R$ {produtos[cont]:>6.2f}')   # alinhado à direita em 6 espaços, 2 pontos flutuantes
print('-'*45)
