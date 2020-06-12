lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')   # NÃO MOSTRA A POSIÇÃO

print()   # OU...

for cont in range(0, len(lanche)):   # LEN(LANCHE) = 5 ... COMO ELE IGNORA O ÚLTIMO, FAZ DE 0-4
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')   # MOSTRA A POSIÇÃO

print()   # OU...

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')   # MOSTRA A POSIÇÃO

print('Comi pra caramba!')
