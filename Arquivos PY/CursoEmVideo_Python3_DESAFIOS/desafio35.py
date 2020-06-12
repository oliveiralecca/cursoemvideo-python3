print('======= DESAFIO 35 =======')
print()
print('{:=^30}'.format(' TRIÂNGULOS '))
r1 = float(input('Comprimento da Reta 1: '))
r2 = float(input('Comprimento da Reta 2: '))
r3 = float(input('Comprimento da Reta 3: '))
if (r1 < r2 + r3) and (r2 < r3 + r1) and (r3 < r1 + r2):
    print('Podem formar um TRIÂNGULO!')
else:
    print('NÃO PODEM formar um triângulo!')
print('='*30)
