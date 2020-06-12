print('======= DESAFIO 23 =======')
num = int(input('Digite um número inteiro de 0 a 9999: '))
# print('Unidade:', num[3])
# print('Dezena:', num[2])
# print('Centena:', num[1])
# print('Milhar:', num[0])
# => SÓ FUNCIONA COM NÚMEROS DE 4 DÍGITOS

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
