n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

# print('A soma vale {}'.format(n1+n2))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.2f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira é {} e potência é {}'.format(di, e))

# end=' ' => não quebra a linha
# \n => quebra de linha


