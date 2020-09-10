# n = s = 0
# while n != 999:   # FLAG (PONTO DE PARADA)
#     n = int(input('Digite um número: '))
#     s += n
# s -= 999   # GAMBIARRA PARA O FLAG NÃO ENTRAR NA SOMA!!!
# print('A soma vale {}'.format(s))

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')   # F-STRING = atualização do print a partir do Python 3.6
