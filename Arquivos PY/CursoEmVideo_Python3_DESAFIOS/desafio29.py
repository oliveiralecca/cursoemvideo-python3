print('======= DESAFIO 29 =======')
print()
print('{:=^30}'.format(' VELOCÍMETRO '))
vel = float(input('Velocidade do carro (km/h): '))
if vel > 80:
    print('{:^30}\nVocê foi MULTADO por excesso de velocidade!'.format('!!ATENÇÃO!!'))
    m = (vel - 80) * 7
    print('VALOR DA MULTA: R${:.2f}'.format(m))
else:
    print('Tenha um bom dia, e dirija com segurança!')
print('='*30)
