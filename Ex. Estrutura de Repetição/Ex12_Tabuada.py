print('Exercício 12 - Tabuada até o 10')

numero = int(input('Insira um número para calcular a tabuada:\n'))

for counter in range(1, 11):
    resultado = round(numero * counter)
    print(f'{numero} X {counter} = {resultado}')
