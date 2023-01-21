print('Exercício 20')
numero = int(input('Insira um número:\n'))
resultado = 1

if 0 < numero < 16:
    for contador in range(1, numero + 1):
        resultado *= contador
    print(f'{numero}! = {resultado}')
else:
    print('Fatorial fora do limite')
