print('======= DESAFIO 14 =======')
c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32

# também pode ser escrito sem parêntese nenhum: ordem de precedência!

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(c, f))
