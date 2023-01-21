print('Exercício 26')

qtd_pessoas = 5
candidatoA = 0
candidatoB = 0
candidatoC = 0

for counter in range(1,qtd_pessoas + 1):
    voto = input('Escolha seu canditado (A/B/C):\n')

    if voto == 'A':
        candidatoA += 1
    elif voto == 'B':
        candidatoB += 1
    elif voto == 'C':
        candidatoC += 1
    else:
        print('Voto inválido')

print(f'O candidato A recebeu {candidatoA} votos')
print(f'O candidato B recebeu {candidatoB} votos')
print(f'O candidato C recebeu {candidatoC} votos')