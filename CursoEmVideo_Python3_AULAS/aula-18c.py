galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in galera:
    print(p)   # MOSTRA AS 4 LISTAS COMPLETAS

print()

for p in galera:
    print(p[0])   # MOSTRA OS NOMES

print()

for p in galera:
    print(p[1])   # MOSTRA AS IDADES

print()

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')   # NOMES E IDADES DE CADA UM
