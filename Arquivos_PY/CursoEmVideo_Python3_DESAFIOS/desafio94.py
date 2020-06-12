print('-=-=-=-= DESAFIO 94 -=-=-=-=')
print()

print('=-='*15)
print(f'{"CADASTRO DE PESSOAS":^45}')
print('=-='*15)

pessoa = {}
lista = []
totidade = media = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    totidade += pessoa['idade']
    lista.append(pessoa.copy())
    print('-'*45)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    print('-'*45)
    if continuar == 'N':
        break

print(f' A) O grupo tem {len(lista)} pessoas.')
media = totidade / len(lista)
print(f' B) A média de idade é de {media:.1f} anos.')
print(' C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print(' D) Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k.title()} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
