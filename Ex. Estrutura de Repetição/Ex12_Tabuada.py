print('Exercício 12 - Tabuada até o 10')

numero = int(input('Insira um número para calcular a tabuada:\n'))

print(f'Tabuada do {numero}:')
for counter in range(1, 11):
    resultado = round(numero * counter)
    print(f'{numero} X {counter} = {resultado}')
