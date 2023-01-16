from datetime import datetime

print('Exercício 18: Validação datas')

data = input('Escreva uma data no formato (dd/MM/aaaa):\n')
try:
    datetime.strptime(data, '%d/%m/%Y')
    print('Data inserida está válida')
except ValueError:
    print('Formato inválido. Escreva dd/MM/yyyy')