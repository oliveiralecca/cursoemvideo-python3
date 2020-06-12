print('======= DESAFIO 15 =======')
print('----- OLIV LOCADORA DE CARROS -----')
dias = int(input('Por quantos dias foi alugado: '))
km = float(input('Quantos km percorridos: '))
p = (60 * dias) + (0.15 * km)
print()
print('Total a pagar: R${:.2f}'.format(p))
print('-----------------------------------')

