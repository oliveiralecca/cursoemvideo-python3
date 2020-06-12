print('-=-=-=-= DESAFIO 83 -=-=-=-=')
print()

a = []
b = []

exp = str(input('Digite sua expressão: '))
for e in exp:
    if e == '(':
        a.append('(')
    elif e == ')':
        b.append(')')

if len(a) == len(b):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

# RESOLUÇÃO do PROF:
# pilha = []
# for e in exp:
#     if e == '(':
#         pilha.append('(')
#     elif e == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('Expressão válida!')
# else:
#     print('Expressão errada!')
