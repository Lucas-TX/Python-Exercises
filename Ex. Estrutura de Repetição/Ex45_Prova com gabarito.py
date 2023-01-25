from tabulate import tabulate
import os
import re

mensagem_votacao = '''
Escolha o código do seu candidato.
Digite 0 para encerrar a votação. 

'''
head_canditados = ['Código canditado', 'Descrição']
tabela_candidatos = [
    [1, 'candidato A'],
    [2, 'candidato B'],
    [3, 'candidato C'],
    [4, 'candidato D'],
    [5, 'Nulo'],
    [6, 'Branco'],
    [9, 'Ajuda'],
    [0, 'Encerrar']
]
print(tabulate(tabela_candidatos, headers=head_canditados))
head_votacao = ['Canditado', 'Votos', 'Votos(%)', 'Votos válidos(%)']
tabela_votacao = [
    ['1 - candidato A', 0, 0, 0],
    ['2 - candidato B', 0, 0, 0],
    ['3 - candidato C', 0, 0, 0],
    ['4 - candidato D', 0, 0, 0],
    ['Nulo', 0, 0, 0],
    ['Branco', 0, 0, 0],
    ['Total', 0, 0, 0],
]

while True:
    try:
        voto = int(input('Escreva o código do seu candidato: '))
    except ValueError:
        print('Opção inválida. Tente novamente.')
        continue

    match voto:
        case 0:
            print(f'Votação encerrada.')
            break
        case 1:
            nome_candidato = tabela_votacao[0][0]
            tabela_votacao[0][1] += 1
        case 2:
            nome_candidato = tabela_votacao[1][0]
            tabela_votacao[1][1] += 1
        case 3:
            nome_candidato = tabela_votacao[2][0]
            tabela_votacao[2][1] += 1
        case 4:
            nome_candidato = tabela_votacao[3][0]
            tabela_votacao[3][1] += 1
        case 5:
            print(f'Voto nulo.')
            tabela_votacao[4][1] += 1
        case 6:
            print(f'Voto Branco.')
            tabela_votacao[5][1] += 1
        case 9:
            os.system('cls')
            print(mensagem_votacao)
            continue
        case _:
            print(f'Candidato não encontrado. Voto nulo.')
            tabela_votacao[4][1] += 1

total_votos = 0
total_validos = 0
for row in tabela_votacao:
    votos = int(row[1])
    total_votos += votos
    if re.search("^\d", row[0]):
        total_validos += votos

tabela_votacao[6][1] = total_votos
tabela_votacao[6][3] = 100

for row in tabela_votacao:
    row[2] = (int(row[1]) / total_votos) * 100

    if re.search("^\d", row[0]):
        row[3] = (row[1] / total_validos) * 100

print(tabulate(tabela_votacao, headers=head_votacao))
