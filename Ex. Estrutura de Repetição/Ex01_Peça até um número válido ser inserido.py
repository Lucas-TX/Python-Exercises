print('Exercício 1')
while True:
    nota = float(input('Insira uma nota entre 0 e 10:\n'))
    if  0 < nota < 10:
        print(f'Nota: {nota}')
        break
    else:
        print('Nota inválida. Tente novamente.')