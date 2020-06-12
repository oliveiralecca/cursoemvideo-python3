print('-=-=-=-= DESAFIO 64 -=-=-=-=')
print()
n = tot = soma = 0
print('Para sair, digite "999".')
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        tot += 1
        soma += n
print('Foram digitados {} valores e a soma entre eles vale {}.'.format(tot, soma))

# RESOLUÇÃO do PROF:
# n = int(input('Digite um número [999 para sair]: '))
# while n != 999:
#     tot += 1
#     soma += n
#     n = int(input('Digite um número [999 para sair]: '))
# print('Foram digitados {} valores e a soma entre eles vale {}.'.format(tot, soma))
