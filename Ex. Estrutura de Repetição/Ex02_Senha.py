print('Exercício 2')
while True:
    usuario = input('Insira seu usuário:\n')
    senha = input('Insira sua senha:\n ')

    if senha != usuario:
        print(f'Senha Válida')
        break
    else:
        print('Senha inválida. Tente novamente.')