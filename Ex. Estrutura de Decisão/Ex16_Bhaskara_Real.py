import math
print('Exercício 16: Bhaskara')
a = float(input("Informe o coeficiente 'a'\n"))
b = float(input("Informe o coeficiente 'b'\n"))
c = float(input("Informe o coeficiente 'c'\n"))

if a == 0:
    print('Equação não é do Segundo grau, pois a = 0')
    exit()

delta = b ** 2 - 4 * a * c
if delta < 0:
    print('A equação não possui raízes reais. Fórmula de Bhaskara não será realizada')
    exit()

x1 = ((-1) * b + math.sqrt(delta))/2 * a
x2 = ((-1) * b - math.sqrt(delta))/2 * a

if delta == 0:
    print('Como delta = 0, a equação possui apenas uma raíz.')
    print(f'x1 = x2 = {x1}')
else:  # delta > 0, há duas raízes reais
    print(f'x1 = {x1}\nx2 = {x2}')
