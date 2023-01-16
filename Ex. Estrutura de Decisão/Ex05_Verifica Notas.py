print('Exercício 5: Verifica notas parciais e calcula média')
notaParcial1 = input('Informe a primeira nota parcial:\n')
notaParcial2 = input('Informe a segunda nota parcial:\n')
media = (float(notaParcial1) + float(notaParcial2))/2
if media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com distinção')
else:
    print('Aprovado')
