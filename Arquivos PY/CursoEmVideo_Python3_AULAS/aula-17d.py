a = [2, 3, 4, 7]
# b = a   # CRIA UMA LIGAÇÃO ENTRE AS LISTAS, NÃO UMA CÓPIA. SE MUDO OS ELEMENTOS DE UMA, TB MUDA NA OUTRA
b = a[:]   # CRIA UMA CÓPIA (b recebe todos os elementos de a  >>  [:] não sei o ínicio, nem o fim)
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
