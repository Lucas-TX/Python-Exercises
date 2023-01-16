print('Exercício 1: Mostre o maior número')
numero1 = input('Insira o primeiro número:\n')
numero2 = input('Insira o primeiro número:\n')

if float(numero1) > float(numero2):
    print(numero1, '>', numero2)
elif float(numero1) == float(numero2):
    print(numero1, '=', numero2)
else:
    print(numero2, '>', numero1)
