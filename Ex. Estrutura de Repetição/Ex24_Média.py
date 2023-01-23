print('Exercício 24')

contador = 0
soma = 0
print('Quando não quiser inserir mais notas, digite 0.')
while True:
    try:
        nota = float(input('Insira a nota: '))
    except ValueError:
        print('Insira um número.')
        continue
    if nota == 0:
        break
    contador += 1
    soma += nota
media = soma/contador
print(f'Média das {contador} notas é {round(media,2)}.')


