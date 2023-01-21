print('Exercício 21 e 22')

# numero = int(input('Insira um número:\n'))
numero = 29
flag_divisor = False

if numero == 1:
    flag_divisor = True

for contador in range(2, numero):
    if numero % contador == 0:
        print(f'{contador} é um divisor de {numero}')
        flag_divisor = True

if flag_divisor == True:
    print(f'{numero} não é um número primo.')
else:
    print(f'{numero} é um número primo.')
