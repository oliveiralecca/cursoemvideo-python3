nome = str(input('Qual é seu nome? ')).title()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))

# RESUMÃO DE CONDIÇÕES:

# if _______:
# CONDIÇÃO SIMPLES

# if _______:
# else:
# CONDIÇÃO COMPOSTA

# if _______:
# elif _______:
# elif _______:
# .....
# else: (OPCIONAL)
# CONDIÇÕES ANINHADAS
