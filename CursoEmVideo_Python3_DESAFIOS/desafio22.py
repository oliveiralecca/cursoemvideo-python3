print('======= DESAFIO 22 =======')
nome = input('Digite seu nome completo: ')
print('MAIÚSCULO:', nome.upper())
print('minúsculo:', nome.lower())
lista = nome.split()
lista2 = ''.join(lista)
print('Quantidade de letras (s/ espaços):', len(lista2))
print('Quantidade de letras do primeiro nome:', len(lista[0]))

# ou:
# nome = input('Digite seu nome completo: ').strip()
# print('Seu nome tem no total {} letras'.format(len(nome) - nome.count(' ')))
# print ('Seu primeiro nome tem {} letras'.format(nome.find(' '))) => mostra a posição do primeiro espaço
