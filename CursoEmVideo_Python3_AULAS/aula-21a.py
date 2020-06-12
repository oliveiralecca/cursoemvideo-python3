def fatorial(num=1):   # PARÂMETRO OPCIONAL: SE EU NÃO INFORMARNO PROGR PRINC, ELE VALERÁ 1
    f = 1   # VARIÁVEL LOCAL
    for c in range(num, 0, -1):
        f *= c
    return f   # PODE RETORNAR VALOR LÓGICO, INT, FLOAT, STR, TUPLAS, LISTAS, DICIONÁRIOS...


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')

print()

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
