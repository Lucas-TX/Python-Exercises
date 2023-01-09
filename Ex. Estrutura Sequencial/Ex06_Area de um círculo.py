import math

print('Exercício 6: Área de um círculo com o raio')
raio = input('Informe o raio do círculo (metros): \n')
area = round(math.pi * float(raio)**2,2)
print('A área do círculo é: ', area, ' metros')
