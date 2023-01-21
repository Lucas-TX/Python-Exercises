print('Exercício 25')

# qtd_pessoas = int(input('Insira a quantidade de pessoas:\n'))
qtd_pessoas = 5

soma = 0
for counter in range(1, qtd_pessoas + 1):
    idade = int(input(f'Insira a idade da {counter}° pessoa:\n'))
    soma += idade

media = soma/qtd_pessoas

if 0 < media <= 25:
    print('A turma é jovem')
elif 25 < media <= 60:
    print('A turma é adulta')
elif media > 60:
    print('A turma é idosa')
