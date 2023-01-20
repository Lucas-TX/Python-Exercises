print('Exercício 15,16 e 17')

ultimo = 1
penunultimo = 1

termo_limite = int(input('Insira o termo desejado:\n'))

if termo_limite == 1:
    print('Soma: 1')
    print('Termo: 1')
    exit()
if termo_limite == 2:
    print('Soma: 2')
    print('Termo: 2')
    exit()

for termo in range(2,termo_limite ):
    resultado = ultimo + penunultimo
    penunultimo = ultimo
    ultimo = resultado
    termo += 1

print(f'Soma: {resultado}')
print(f'Termo: {termo}')

