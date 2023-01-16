print('Exercício 13: Triângulo')
lado1 = float(input('Insira o primeiro lado do triângulo:\n'))
lado2 = float(input('Insira o segundo lado do triângulo:\n'))
lado3 = float(input('Insira o terceiro lado do triângulo:\n'))

if lado1 == lado2 == lado3:
    print('Triângulo equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Triângulo isóceles')
elif lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Triângulo escaleno')
else:
    print('Não forma triângulo')
