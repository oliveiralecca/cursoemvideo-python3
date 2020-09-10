# potência = 4**3 = pow(4,3)
# raiz quadrada = 81**(1/2)
# raiz cúbica = 81**(1/3)
# 'Oi' + 'Olá' = 'OiOlá' => concatenação

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print("Prazer em te conhecer, {:<20}!".format(nome))
print("Prazer em te conhecer, {:^20}!".format(nome))
print('Prazer em te conhecer, {:=^20}!'.format(nome))
