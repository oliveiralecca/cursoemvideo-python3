print('-=-=-=-= DESAFIO 37 -=-=-=-=')
print()
print('{:=^50}'.format(' CONVERSOR DE BASES NUMÉRICAS '))
num = int(input('Digite um número inteiro: '))
print('''ESCOLHA A BASE DE CONVERSÃO
 [1] Binário\n [2] Octal\n [3] Hexadecimal''')
escolha = int(input('OPÇÃO: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num))[2:])
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA!')
print('='*50)
