print('======= DESAFIO 31 =======')
print()
print('{:=^30}'.format(' e-TICKET '))
d = float(input('Distância da sua viagem (km): '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('Preço da passagem: R${:.2f}'.format(p))
print('='*30)

# RESOLUÇÃO do PROF:
# p = d * 0.5 if d <= 200 else d * 0.45
