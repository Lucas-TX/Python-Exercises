print('''
Exercício 11: Com base em 2 números inteiros e 1 Real, calcule e mostre:
    a. Produto do dobro do primeiro com metade do segundo.
    b. Soma do triplo do primeiro com o terceiro.
    c. Terceiro elevado ao cubo.
''')

inteiro_1 = input('Escreva o primeiro número inteiro:\n')
inteiro_2 = input('Escreva o segundo número inteiro:\n')
num_Real = input('Escreva o número real:\n')

calculo_a = (int(inteiro_1)*2)*(int(inteiro_2)/2)
calculo_b = (int(inteiro_1)*3) + float(num_Real)
calculo_c = float(num_Real)**3

print('Cálculo A: ', calculo_a)
print('Cálculo B: ', calculo_b)
print('Cálculo C: ', calculo_c)
