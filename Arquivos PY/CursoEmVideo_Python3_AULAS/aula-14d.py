n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:   # PARA QUE O 0 QUE INDICA O FIM DO PROGRAMA, NÃO SEJA CONSIDERADO NA CONTAGEM!
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números PARES e {} números ÍMPARES!'.format(par, impar))
