print('Exercício 11: Calcule o reajuste salarial dos trabalhadores')
salario = float(input('Escreva o salário do trabalhador:\n'))
print('Salário antes do reajuste:', salario)

if salario <= 280:
    fatorReajuste = 0.2
elif 280 < salario <= 700:
    fatorReajuste = 0.15
elif 700 < salario <= 1500:
    fatorReajuste = 0.10
else:
    fatorReajuste = 0.05

print(f'Foi aplicado {fatorReajuste*100}% de reajuste.\n'
      f'O salário vai aumentar R${round(fatorReajuste*salario,2)}.\n'
      f'Após o aumento, o salário final será: {round(salario * (1+fatorReajuste),2)}')
