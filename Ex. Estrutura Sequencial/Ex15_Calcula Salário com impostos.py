print('Exercício 15: Calcular Salário considerando os impostos.')
salarioPorHora = input('Qual é o seu valor por hora?\n')
horasTrabalhadas = input('Quantas horas foram trabalhadas:\n')
salarioBruto = float(salarioPorHora) * float(horasTrabalhadas)
impostoDeRenda = salarioBruto * 0.11
valor_INSS = salarioBruto * 0.08
valor_sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - impostoDeRenda - valor_INSS - valor_sindicato
print('O salário bruto é ', round(salarioBruto, 2))
print('O imposto de renda retido na fonte é ', round(impostoDeRenda, 2))
print('O contribuição com o INSS é ', round(valor_INSS, 2))
print('O contribuição sindical é ', round(valor_sindicato, 2))
print('O salário líquido é ', round(salarioLiquido, 2))
