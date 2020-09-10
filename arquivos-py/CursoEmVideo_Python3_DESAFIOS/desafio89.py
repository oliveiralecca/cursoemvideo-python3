print('-=-=-=-= DESAFIO 89 -=-=-=-=')
print()

from time import sleep
sala = []
dadosnome = []
dadosnota = []

while True:
    dadosnome.append(str(input('Nome do aluno(a): ')))
    dadosnota.append(float(input('Nota 1: ')))
    dadosnota.append(float(input('Nota 2: ')))
    dadosnome.append(dadosnota[:])
    sala.append(dadosnome[:])
    dadosnome.clear()
    dadosnota.clear()
    print('-'*25)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('-'*25)

print('=-='*20)
print(f'{"Nº":<4} {"ALUNO":<15} {"MÉDIA":<10}')
print('-'*30)
for i, aluno in enumerate(sala):
    m = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{i:<5}', end='')
    print(f'{aluno[0]:<16}', end='')
    print(f'{m:>5.1f}')
print('-'*40)

while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for i, aluno in enumerate(sala):
        if notas == i:
            print(f'Notas de {aluno[0]} são {aluno[1]}')
    if notas == 999:
        print()
        break
    print('-' * 40)
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')


# RESOLUÇÃO do PROF:
# ficha = list()
# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
# [. . .]
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if notas == 999:
#         print('FINALIZANDO...')
#         break
#     if notas <= len(ficha) - 1:
#         print(f'Notas de {fichas[notas][0]} são {ficha[notas][1]}')
