# valores = list()   # PODE CRIAR UMA LISTA VAZIA DAS DUAS MANEIRAS
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

print()
print()

for i, v in enumerate(valores):
    print(f'Na posição {i} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
