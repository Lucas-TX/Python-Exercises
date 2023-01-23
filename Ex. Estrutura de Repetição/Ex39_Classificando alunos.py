print('Exercício 39')

dic_alunos = {}

for iterador in range(1, 11):
    numero_aluno = input(f'Insira o número do aluno {iterador}: ')
    altura_aluno = int(input(f'Insira a altura,em centímetros, do aluno {iterador}: '))
    dic_alunos[numero_aluno] = altura_aluno

maior_aluno = int(list(dic_alunos.values())[0])
menor_aluno = int(list(dic_alunos.values())[0])
for numero, altura in dic_alunos.items():
    if altura > maior_aluno:
        maior_aluno = altura
    if altura < menor_aluno:
        menor_aluno = altura

print(f'O maior aluno é o {list(dic_alunos.keys())[list(dic_alunos.values()).index(maior_aluno)]}. '
      f'A altura dele é {maior_aluno} centímetros')
print(f'O menor aluno é o {list(dic_alunos.keys())[list(dic_alunos.values()).index(menor_aluno)]}.'
      f' A altura dele é {menor_aluno} centímetros')
