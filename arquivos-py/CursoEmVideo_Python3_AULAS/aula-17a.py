# PARA VER CADA COMANDO FUNCIONANDO, COLOCAR OS DEMAIS COMO COMENTÁRIO!
num = [2, 5, 9, 1]

num[2] = 3   # LISTAS SÃO MUTÁVEIS
num.append(7)   # ADICIONA O Nº AO FINAL DA LISTA
num.sort()   # COLOCA EM ORDEM
num.sort(reverse=True)   # COLOCA EM ORDEM INVERSA
num.insert(2, 3)   # ADICIONA 3 NA POSIÇÃO 2
num.pop()   # ELIMINA O ÚLTIMO VALOR
num.pop(1)   # ELIMINA O ELEMENTO DA POSIÇÃO 1
num.remove(2)   # ELIMINA O VALOR 2 EM SUA PRIMEIRA OCORRÊNCIA
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

print(num)
print(f'Essa lista tem {len(num)} elementos.')
