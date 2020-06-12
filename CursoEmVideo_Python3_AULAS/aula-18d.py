galera = []   # ESTRUTURA PRINCIPAL
dado = []   # ESTRUTURA AUXILIAR, SÓ PARA COLETAR OS DADOS
totmaior = totmenor = 0   # !CUIDADO!: SÓ PODE FAZER ESSA IGUALDADE COM VARIÁVEIS SIMPLES

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])   # SE ESQUECER DE CRIAR UMA CÓPIA DOS DADOS USANDO [:],
    dado.clear()   # ..., VAI GERAR LISTAS VAZIAS, POIS COMO ESTÃO LIGADAS E MANDEI APAGAR UMA DELAS, AS 2 SÃO APAGADAS!
# print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade!')
