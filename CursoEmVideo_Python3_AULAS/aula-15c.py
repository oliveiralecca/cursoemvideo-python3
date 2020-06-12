# MAIS EXEMPLOS DE F-STRING:

nome = ' José '
idade = 33
salario = 987.3
# print('O {} tem {} anos.'.format(nome, idade))   # PYTHON 3
print(f'O {nome:=^20} tem {idade} anos e ganha R${salario:.2f}')   # PYTHON 3.6+
