print('Exercício 21: Caixa Eletrônico')
saque = int(input('Qual é o valor do saque desejado:\n'))
# Verifica mínimo e máximo permitido
if saque < 10 or saque > 600:
    print('O saque deve ser, no mínimo, R$10 e, no máximo, R$600.')
    exit()

notas100 = saque // 100
saque -= notas100 * 100
notas50 = saque // 50
saque -= notas50 * 50
notas20 = saque // 20
saque -= notas20 * 20
notas10 = saque // 10
saque -= notas10 * 10
notas5 = saque // 5
saque -= notas5 * 5

print(f'{notas100} de R$100')
print(f'{notas50} de R$50')
print(f'{notas20} de R$20')
print(f'{notas10} de R$10')
print(f'{notas5} de R$5')
print(f'{saque} de R$1')



