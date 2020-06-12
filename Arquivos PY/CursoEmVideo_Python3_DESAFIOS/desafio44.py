print('-=-=-=-= DESAFIO 44 -=-=-=-=')
print()
print('{:=^40}'.format(' PAGAMENTOS '))
p = float(input('Preço das compras: R$'))
print()
print('''CONDIÇÃO DE PAGAMENTO 
 [1] à vista DINHEIRO/CHEQUE\n [2] à vista CARTÃO\n [3] em até 2x no CARTÃO\n [4] 3x ou mais no CARTÃO''')
escolha = int(input('OPÇÃO: '))
print()
if escolha == 1:
    np = p - (p * 10/100)
    print('Valor a ser pago: {}R${:.2f}{}'.format('\033[31m', np, '\033[m'))
elif escolha == 2:
    np = p - (p * 5/100)
    print('Valor a ser pago: {}R${:.2f}{}'.format('\033[31m', np, '\033[m'))
elif escolha == 3:
    np = p
    print('Valor a ser pago: {}R${:.2f}{}'.format('\033[31m', np, '\033[m'))
elif escolha == 4:
    np = p + (p * 20/100)
    print('Valor a ser pago: {}R${:.2f}{}'.format('\033[31m', np, '\033[m'))
else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')
print('='*40)
