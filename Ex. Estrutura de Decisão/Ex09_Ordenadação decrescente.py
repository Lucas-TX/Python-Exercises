print('Exercício 9: Mostre os números em ordem decrescente')

quantidade_Execucoes = input('Insira a quantidade de números em que se deseja ordenar:\n')

list_numeros = []

for i in range(int(quantidade_Execucoes)):
    numero = input('Insira um número:\n')
    list_numeros.append(float(numero))
list_numeros.sort(reverse=True)
print(*list_numeros, sep=",")
