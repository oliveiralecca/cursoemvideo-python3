a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a   # DIFERENTE DE a + b
print(c)

print()

print(len(c))   # QUANTOS ELEMENTOS
print(c.count(5))   # QUANTAS VEZES APARECE
print(c.index(2))  # EM QUE POSIÇÃO ESTÁ A PRIMEIRA OCORRÊNCIA
print(c.index(5, 1))   # EM QUE POSIÇÃO ESTÁ, COMEÇANDO DA POSIÇÃO 1
