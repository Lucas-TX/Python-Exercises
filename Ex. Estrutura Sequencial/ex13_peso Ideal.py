print('Exercício 13: Calcule o peso ideal')
altura_h = input('Escreva sua altura (metros):\n')
sexo = input('É do sexo masculino?(S/N)\n')
if sexo == 'S':
    peso_Ideal = (72.7*float(altura_h)) - 58
elif sexo == 'N':
    peso_Ideal = (62.1 * float(altura_h)) - 44.7
else:
    print("Insira 'S' ou 'N' quando pedir o sexo.")
    exit()
print("O seu peso ideal é: ", peso_Ideal)
