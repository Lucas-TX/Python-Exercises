print('Exercício 35')

numero = 1
lista_primos = [numero]
flag_primo = True
while True:
    try:
        numero = int(input('Insira o número inteiro do limite superior: '))
        break
    except ValueError:
        print('O número deve ser inteiro.')
        continue

for num in range(2, numero + 1):
    flag_primo = True
    for contador in range(2, num):
        if num % contador == 0:
            flag_primo = False
            break
    if flag_primo:
        # print(f'O número {num} é primo. Adicionando na lista de primos')
        lista_primos.append(num)
print(f'Primos: {lista_primos}')
