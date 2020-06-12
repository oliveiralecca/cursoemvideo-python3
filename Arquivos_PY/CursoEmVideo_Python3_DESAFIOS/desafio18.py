from math import cos, sin, tan, radians
print('======= DESAFIO 18 =======')
ang = float(input('Digite um ângulo qualquer: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(sen, coss, tang))
