# TRATAMENTO DE ERRO
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema :(')   # DEU ERRADO
else:
    print(f'O resultado é {r:.1f}')   # DEU CERTO
finally:
    print('Volte sempre! Muito obrigada!')   # ACONTECE SEMPRE, INDEPENDENTE DE DAR CERTO OU ERRADO
