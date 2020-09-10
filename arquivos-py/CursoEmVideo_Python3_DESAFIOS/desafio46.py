from time import sleep
import emoji
print('-=-=-=-= DESAFIO 46 -=-=-=-=')
print()
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[33m:boom:\033[m FELIZ ANO NOVO!! \033[33m:boom:\033[m', use_aliases=True))
