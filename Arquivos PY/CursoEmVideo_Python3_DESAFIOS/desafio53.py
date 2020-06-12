print('-=-=-=-= DESAFIO 53 -=-=-=-=')
print()
print('{:=^60}'.format(' PALÍNDROMOS '))
frase = str(input('Digite uma frase: ')).strip().upper()   # tira espaços antes e dps, e bota em MAIÚSC
palavras = frase.split()   # faz uma lista
junto = ''.join(palavras)   # junta a lista sem espaço entre palavras
inverso = junto[::-1]   # faz a palavra ao contrário
if junto == inverso:
    print('{} e {} são iguais, É um Palíndromo!'.format(junto, inverso))
else:
    print('{} e {} não são iguais, NÃO É um Palíndromo!'.format(junto, inverso))
print('='*60)

# RESOLUÇÃO do PROF:
# inverso = ''
# for c in range(len(junto)-1, -1, -1):
#    inverso += junto[c]
# print('O inverso de {} é {}'.format(junto, inverso))
# if inverso == junto:
#    print('Temos um palíndromo!')
# else:
#    print('Não é um palíndromo!')
