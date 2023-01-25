from tabulate import tabulate
print('Exercício 41')

head_parcela_juros = ['Quantidade de parcelas mesais', 'Juros mensais(%)']
head_calculo_divida = ['Valor da dívida', 'Valor dos juros mensal(%)', 'Quantidade de parcelas', 'Valor da parcela']
dados_parcela_juros = [
    [1, 0],
    [3, 10],
    [6, 15],
    [9, 20],
    [12, 25]
]
dados_calculo_divida = []
# divida = input('Escreva o valor da dívida: ')
divida = 1000


for row in dados_parcela_juros:
    qtd_parcelas = row[0]
    juro = 1 + row[1]/100
    montante = round(divida * juro, 2)
    valor_parcela = round(montante / qtd_parcelas, 2)
    dados_calculo_divida.append([montante, row[1], qtd_parcelas, valor_parcela])

print('Planilha de juros')
print(tabulate(dados_parcela_juros, headers=head_parcela_juros))
print('\n')
print('Planilha descritivo da dívida')
print(tabulate(dados_calculo_divida, headers=head_calculo_divida))
