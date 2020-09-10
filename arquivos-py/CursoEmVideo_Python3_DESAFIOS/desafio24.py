print('======= DESAFIO 24 =======')
cid = input('Digite o nome de uma cidade: ')
lista = cid.title().split()
print('Ela começa com o nome Santo? ', 'Santo' in lista[0])

# ou:
# cid = input('Digite o nome de uma cidade: ').strip()
# print(cid[:5].upper() == 'SANTO')
