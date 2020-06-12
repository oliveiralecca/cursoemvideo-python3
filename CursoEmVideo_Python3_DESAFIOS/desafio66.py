print('-=-=-=-= DESAFIO 66 -=-=-=-=')
print()

s = tot = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    tot += 1
print(f'A soma entre os {tot} valores digitados é igual a {s}!')
