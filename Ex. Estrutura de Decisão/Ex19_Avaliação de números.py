print('Exercício 19: Avaliação de números')
numero_original = int(input('Insira um número inteiro até 1000:\n'))

mensagem_centenas = ''
mensagem_dezenas = ''
mensagem_unidades = ''
mensagem = ''

centenas = numero_original // 100
if centenas > 1:
    mensagem_centenas = f'{centenas} centenas'
elif centenas == 1:
    mensagem_centenas = f'{centenas} centena'
else:  # centenas = 0
    pass

numero = numero_original - centenas * 100
dezenas = numero // 10
if dezenas > 1:
    mensagem_dezenas += f'{dezenas} dezenas'
elif dezenas == 1:
    mensagem_dezenas += f'{dezenas} dezena'
else:  # Dezenas = 0
    pass

numero = numero - dezenas * 10
if numero > 1:
    mensagem_unidades = f'{numero} unidades'
elif numero == 1:
    mensagem_unidades = f'{numero} unidade'
else:  # número = 0
    pass

if mensagem_centenas:
    mensagem = mensagem_centenas
if mensagem_dezenas and mensagem_unidades:
    if mensagem_centenas:
        mensagem += ','
    mensagem += mensagem_dezenas + ' e ' + mensagem_unidades
else:  # Alguma das duas mensagens é falsa
    if mensagem_dezenas:
        if mensagem_centenas:
            mensagem += ' e '
        mensagem += mensagem_dezenas
    elif mensagem_unidades:
        if mensagem_centenas:
            mensagem += ' e '
        mensagem += mensagem_unidades
    else:  # As duas mensagens são falsas
        pass
print(f'{numero_original} = {mensagem}')
