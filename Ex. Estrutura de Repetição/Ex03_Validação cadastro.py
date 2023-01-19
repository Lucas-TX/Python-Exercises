print('Exercício 3')

#  Validação do nome
while True:
    nome = input('Escreva seu nome:\n')
    if len(nome) > 3:
        break
    else:
        print('Nome deve ser maior do que 3 caracteres.')

# Validação da idade
while True:
    idade = int(input('Escreva sua idade:\n'))
    if 0 < idade < 150:
        break
    else:
        print('Nome deve ser maior do que 0 e menor do que 150.')

# Validação do salário
while True:
    salario = float(input('Escreva seu salário:\n'))
    if salario > 0:
        break
    else:
        print('Salário deve ser maior do que 0.')

# Validação do sexo
while True:
    sexo = input('Escreva seu sexo(f/m):\n')
    if sexo == 'f' or sexo == "m":
        break
    else:
        print("Sexo deve ser 'f' ou 'm'.")

# Validação do estado Civil
while True:
    estadoCivil = input('Escreva seu estado civil:\nSolteiro(s)\nCasado(c)\nViúvo(v)\nDivorciado(d)\n')
    if estadoCivil == 's' or estadoCivil == 'c' or estadoCivil == 'v' or estadoCivil == 'd':
        break
    else:
        print("Estado civil deve ser (s/c/v/d)")
