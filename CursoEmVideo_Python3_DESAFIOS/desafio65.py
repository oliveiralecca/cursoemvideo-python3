print('-=-=-=-= DESAFIO 65 -=-=-=-=')
print()
r = 'S'
soma = tot = m = maior = menor = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('CONTINUAR [S/N]? ')).upper().strip()[0]
    soma += n
    tot += 1
    if tot == 1:   # ou seja, se foi o primeiro N digitado...
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
m = soma / tot
print()
print('A média desses números é igual a {:.2f}.'.format(m))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
