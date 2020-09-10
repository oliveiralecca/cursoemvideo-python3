from math import hypot
print('======= DESAFIO 17 =======')
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hip = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))
