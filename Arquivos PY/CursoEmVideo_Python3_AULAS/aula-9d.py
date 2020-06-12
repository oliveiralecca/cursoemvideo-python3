frase = 'Curso em Vídeo Python'
print('Curso' in frase)   # a palavra 'Curso' entá dentro da frase?
print(frase.find('Curso'))   # mostra a posição de 'Curso'
print(frase.find('Vídeo'))
print(frase.find('video'))   # a palavra em minúsculo e sem acento não existe, então ele mostra -1
