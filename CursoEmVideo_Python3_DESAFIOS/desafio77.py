print('-=-=-=-= DESAFIO 77 -=-=-=-=')
print()

palavras = ('computador', 'apple', 'smartphone', 'starbucks',
            'nubank', 'dobra', 'lenovo', 'capinha', 'iphone',
            'python', 'programar', 'universidade', 'quadro')

for item in palavras:
    print(f'Na palavra {item.upper()} temos', end=' ')
    for letra in item:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
    print()
