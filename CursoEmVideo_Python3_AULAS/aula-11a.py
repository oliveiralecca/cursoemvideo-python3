print('\033[31mOlá, Mundo!')   # letra vermelha
print('\033[1;31;43mOlá, Mundo!\033[m')   # letra negrito; vermelha; fundo amarelo
print('\033[4;31;40mOlá, Mundo!\033[m')   # \033[m  =>  o código vazio, tira todas as formatações
print('\033[4;30;45mOlá, Mundo!\033[m')   # letra sublinhada; branca; fundo lilás
print('\033[7;30mOlá, Mundo!\033[m')   # \033[30m  =>  letra branca; fundo padrão (preto).. o 7 inverte isso
print('\033[7;33;44mOlá, Mundo!\033[m')   # 7 inverte as cores de letra e fundo
