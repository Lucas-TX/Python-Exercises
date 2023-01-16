print('Exercício 17: Ano Bissexto')
ano = input('Informe um ano:\n')

if '00' in ano and int(ano) % 400 == 0:
    print(f'Ano é bissexto')
    exit()

if int(ano) % 4 == 0:
    print(f'Ano é bissexto')
else:
    print('Ano não é bissexto')
