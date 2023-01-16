print('Exercício 12: Folha de pagamento')
valor_hora = float(input('Qual é o seu salário por hora:\n'))
horas_trabalhadas = float(input('Quantas horas foram trabalhadas:\n'))

salario_bruto = valor_hora*horas_trabalhadas
valor_inss = salario_bruto*0.10
valor_fgts = salario_bruto*0.11
valor_sindicato = salario_bruto*0.03
if salario_bruto <= 900:
    valor_impostoRenda = 0
elif 900 < salario_bruto <= 1500:
    valor_impostoRenda = salario_bruto * 0.05
elif 1500 < salario_bruto <= 2500:
    valor_impostoRenda = salario_bruto * 0.10
else: #  Salário Bruto acima de 2500
    valor_impostoRenda = salario_bruto * 0.20
salario_liquido = salario_bruto - valor_impostoRenda - valor_sindicato - valor_inss

print(f'O salário bruto é {salario_bruto}')
print(f'O valor do INSS é {valor_inss}')
print(f'O IR é {valor_impostoRenda}')
print(f'O FGTS é {valor_fgts}')
print(f'A taxa do sindicato é {valor_sindicato}')
print(f'O salário líquido é {salario_liquido}')



