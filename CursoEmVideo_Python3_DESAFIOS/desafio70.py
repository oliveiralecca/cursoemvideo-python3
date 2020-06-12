print('-=-=-=-= DESAFIO 70 -=-=-=-=')
print()

print('='*45)
print('             LOJA SUPER BARATÃO')
print('='*45)

produto = barato = ''
tot = acima = menor = 0
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    if tot == 0 or preco < menor:
        barato = produto
        menor = preco
    # elif preco < menor:
        # barato = produto
        # menor = preco
    tot += preco
    if preco > 1000:
        acima += 1
    print('-'*30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('-'*30)
print()
print('{:=^45}'.format(' FIM DO PROGRAMA '))
print(f'TOTAL DA COMPRA: R${tot:.2f}')
print(f'São {acima} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
