print('-=-=-=-= DESAFIO 80 -=-=-=-=')
print()

num = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-='*15)
print(f'Os valores digitados em ordem foram {num}')
