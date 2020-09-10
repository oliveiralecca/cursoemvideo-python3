print('======= DESAFIO 34 =======')
print()
print('{:=^30}'.format(' CALC DE AUMENTO '))
sal = float(input('Seu salário atual: R$'))
if sal > 1250:
    au = sal + (sal * 10/100)
else:
    au = sal + (sal * 15/100)
print('Seu novo salário é R${:.2f}!'.format(au))
print('='*30)
