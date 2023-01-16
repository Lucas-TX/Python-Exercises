print('Exercício 13: Conceito')
nota1 = float(input('Insira a primeira nota parcial:\n'))
nota2 = float(input('Insira a segunda nota parcial:\n'))
media = (nota1 + nota2)/2

if media == 0:
    conceito = 'F'
    status = 'Reprovado'
elif 0 < media < 4:
    conceito = 'E'
    status = 'Reprovado'
elif 4 <= media < 6:
    conceito = 'D'
    status = 'Reprovado'
elif 6 <= media < 7.5:
    conceito = 'C'
    status = 'Aprovado'
elif 7.5 <= media < 9:
    conceito = 'B'
    status = 'Aprovado'
elif 9 <= media <= 10:
    conceito = 'A'
    status = 'Aprovado'
else:
    print('Notas inválidas')
    exit()

print(f'As notas inseridas foram {nota1} e {nota2}')
print(f'A média é {media}')
print(f'O conceito é {conceito}')
print(f'O aluno foi {status}')
