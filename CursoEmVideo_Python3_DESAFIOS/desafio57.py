print('-=-=-=-= DESAFIO 57 -=-=-=-=')
print()
print('{:=^30}'.format(' VALIDAÇÃO DE DADOS '))
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]   # [0] só a primeira letra, se 'Masculino' ou 'Feminino'
    if sexo != 'M' and sexo != 'F':
        print('Digitação incorreta! Tente novamente.')
    else:
        print('Tudo OK! Obrigada.')
print('='*30)

# RESOLUÇÃO do PROF:
# sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
# while sexo not in 'MF':
#     sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
# print('Sexo {} registrado com sucesso'.format(sexo))
