print('-=-=-=-= DESAFIO 101 -=-=-=-=')
print()


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 15 < idade < 18 or idade > 64:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'


print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
print('-'*30)
