print('Exercício 7: Mostre o maior e o menor número entre 3')
numero1 = input('Insira o primeiro número:\n')
numero2 = input('Insira o segundo número:\n')
numero3 = input('Insira o terceiro número:\n')

if float(numero1) > float(numero2):
    if float(numero1) > float(numero3):
        print(numero1, ' é o maior número')
    else:  # 3 > 1
        print(numero3, ' é o maior número')

    if float(numero2) > float(numero3):
        print(numero3, ' é o menor número')
    else:  # 3 > 2
        print(numero2, ' é o menor número')

else:  # número 2 > 1
    if float(numero2) > float(numero3):
        print(numero2, ' é o maior número')
    else:  # 3 > 2
        print(numero3, ' é o maior número')

    if float(numero1) > float(numero3):
        print(numero3, ' é o menor número')
    else:  # 3 > 2
        print(numero1, ' é o menor número')