from time import sleep
print('-=-=-=-= DESAFIO 106 -=-=-=-=')
print()

cores = ('\033[30;42m',  # 0 - verde
         '\033[30;44m',  # 1 - azul
         '\033[7;30m',  # 2 - branco
         '\033[30;41m',  # 3 - vermelho
         '\033[m')  # 4 - limpa


def titulo(msg, cor=4):
    print(cores[cor], end='')
    print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*(len(msg)+4))
    print(cores[4], end='')


def ajuda(v):
    titulo(f"Acessando o manual do comando '{v}'", 1)
    sleep(1.5)
    print(cores[2], end='')
    help(v)
    print(cores[4], end='')
    sleep(2)

# PROGRAMA PRINCIPAL
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 0)
    escolha = str(input('Função ou Biblioteca > ')).strip()
    if escolha in 'fimFIMFim':
        titulo('ATÉ LOGO!', 3)
        break
    ajuda(escolha)
