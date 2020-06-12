print('======= DESAFIO 26 =======')
frase = input('Digite uma frase: ').strip().lower()
print('A letra A aparece: {} vezes'.format(frase.count('a')))
print('Aparece a 1ª vez na: {}ª posição'.format(frase.find('a') + 1))
print('Aparece a última vez na: {}ª posição'.format(frase.rfind('a') + 1))

# rfind => começa a procurar pela direita (right)
