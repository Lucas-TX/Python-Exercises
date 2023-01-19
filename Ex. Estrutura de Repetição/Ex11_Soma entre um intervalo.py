print('Exercício 9,10 e 11')

# limite_Inferior = 1
# limite_Superior = 50
soma = 0
limite_Inferior = int(input('Insira o limite inferior do intervalo:\n'))
limite_Superior = int(input('Insira o limite Superior do intervalo:\n'))

for counter in range(limite_Inferior, limite_Superior + 1):
    # Exercício 10 - print(f'{counter}')
    # Exercício 9 - if counter % 2 != 0:
        # print(f'{counter} é ímpar')
        # pass
    soma += counter
print(f'Soma: {soma}')
