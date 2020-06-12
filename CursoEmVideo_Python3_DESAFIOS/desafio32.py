print('======= DESAFIO 32 =======')
from datetime import date
print()
print('{:=^30}'.format(' ANO BISSEXTO '))
ano = int(input('Coloque 0 para o ano atual, ou digite o ano: '))
ano2 = str(ano)
if ano == 0:
    ano = date.today().year
print('O ano {} é...'.format(ano))
if (ano2[2:4] == '00') and (ano % 400 == 0) or (ano2[2:4] != '00') and (ano % 4 == 0):
    print('[ ] Normal\n[x] Bissexto')
else:
    print('[x] Normal\n[ ] Bissexto')
print('='*30)

# RESOLUÇÃO do PROF:
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print('ANO BISSEXTO')
