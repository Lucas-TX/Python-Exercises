print('Exercício 14')

qtd_impar = 0
qtd_par = 0

for contador in range(1,11):
    numero = int(input("Escreva um número:\n"))
    if numero % 2 != 0:
        qtd_impar += 1
    else:
        qtd_par += 1

print(f'Foram inseridos {qtd_par} números pares e {qtd_impar} números ímpares.')