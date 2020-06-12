pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

del pessoas['sexo']   # APAGA O ITEM (chave + valor) "SEXO"
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()

pessoas['nome'] = 'Leandro'   # A CHAVE "NOME" PASSA A SER O VALOR "LEANDRO"
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()

pessoas['peso'] = 98.5   # ADICIONO O ITEM "PESO" E SEU VALOR. ESSE MODO SUBSTITUI O .APPEND() DAS LISTAS
for k, v in pessoas.items():
    print(f'{k} = {v}')
