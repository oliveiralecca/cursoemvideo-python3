print('-=-=-=-= DESAFIO 71 -=-=-=-=')
print()

print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 100
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
