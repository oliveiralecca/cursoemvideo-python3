print('-=-=-=-= DESAFIO 90 -=-=-=-=')
print()

aluno = {}

aluno['nome'] = str(input('Nome do aluno(a): ')).title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif aluno['média'] < 5:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'RECUPERAÇÃO'
print('=-='*15)
for k, v in aluno.items():
    print(f'{k.title()} é igual a {v}')
