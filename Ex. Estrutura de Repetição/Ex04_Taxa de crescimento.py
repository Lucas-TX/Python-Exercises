print('Exercício 4 e 5')
maxRetryNumber = 5
anos = 0
# Dados do exercício 4
# pop_cidadeA = int(input(''))
# tx_crescimento_cidadeA = 0.03
# pop_cidadeB = 200000
# tx_crescimento_cidadeB = 0.015
for tentativa in range(1, maxRetryNumber + 1):
    try:
        pop_cidadeA = int(input('Escreva a população da cidade A:'))
        tx_crescimento_cidadeA = float(input('Escreva a taxa anual de crescimento da cidade A:'))
        pop_cidadeB = int(input('Escreva a população da cidade B:'))
        tx_crescimento_cidadeB = float(input('Escreva a taxa anual de crescimento da cidade B:'))

        # Validação da população
        if pop_cidadeA < 0 or pop_cidadeB < 0:
            print('População não pode ser menor do que 0. Tente novamente.')
            continue
        break
    except ValueError:
        print('Isso não é um número válido. Tente novamente')
else:
    print(f'Você excedeu o máximo de {maxRetryNumber} tentativas')
    exit()

# Validação da população
if pop_cidadeA > pop_cidadeB:
    print(f'População da cidade A já é maior do que a população da cidade B.')
    exit()

# Validação da taxa de crescimento
if tx_crescimento_cidadeA < tx_crescimento_cidadeB:
    print(f'A taxa de crescimento da cidade A não pode ser menor do que a taxa de crescimento da cidade B.')
    exit()

while pop_cidadeA <= pop_cidadeB:
    pop_cidadeA = round(pop_cidadeA * (1 + tx_crescimento_cidadeA))
    pop_cidadeB = round(pop_cidadeB * (1 + tx_crescimento_cidadeB))
    anos += 1

print(f'Será necessário {anos} anos para que a população da cidade A iguale ou ultrapasse a da B')
print(f'A:{pop_cidadeA} pessoas\nB:{pop_cidadeB} pessoas')
