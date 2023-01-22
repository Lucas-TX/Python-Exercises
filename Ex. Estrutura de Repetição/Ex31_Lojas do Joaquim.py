import os
print('Exercício 31 - Lojas do Seu joaquim')

maxRetryNumber = 10
mensagemAjuda = f'''Digite 1 para acessar o script da loja quase dois.
Digite 2 para acessar o script da Panificadora.
Digite 3 para acessar o script da loja de conveniência.
Digite 0 para encerrar o programa.
Você tem, no máximo, {maxRetryNumber} tentativas.'''
mensagemMenu = '''Lojas do joaquim
Escolha a loja desejada:
1 - Loja quase dois
2 - Panificadora
3 - Conveniência
8 - Limpar tela
9 - Ajuda
0 - Sair 
-> '''
mensagemValueError = 'Você deve inserir um número válido.'
preco_pao = 0


def loja_quase_dois():
    print('Loja Quase Dois - Tabela de preços')
    for caixa in range(1, 51):
        preco_total = caixa * 1.99
        print(f'{caixa} - R$ {preco_total}')


def panificadora_pao_de_ontem(preco_pao):
    print(f'Preço do pão: {preco_pao}')
    print('Panificadora Pão de Ontem - Tabela de preços')
    for pao in range(1, 51):
        preco_total = pao * preco_pao
        print(f'{pao} - R${round(preco_total,2)}')


def lojas_tabajara():

    soma = 0
    produto = 1
    preco = 1

    print('Lojas Tabajara')
    print('Caixa Registradora')
    print('Escreva o preço dos produtos. Quando finalizar, digite 0 para finalizar a compra')

    while preco != 0:
        try:
            preco = float(input(f'Produto {produto}: R$ '))
        except ValueError:
            print(mensagemValueError)
            continue
        soma += preco
        produto += 1
    print(f'Valor total: R$ {round(soma,2)}')
    valor_pgto = float(input(f'Dinheiro: R$ '))
    if valor_pgto < soma:
        print(f'Valor pago não pode ser menor do que o valor total. Tente novamente.')
    else:
        print(f'Troco: {round(valor_pgto - soma, 2)}')


for tentativa in range(1, maxRetryNumber):
    try:
        opcao = int(input(mensagemMenu))

        match opcao:
            case 1:
                loja_quase_dois()
            case 2:
                preco_pao = float(input('Preço do pão: '))
                panificadora_pao_de_ontem(preco_pao)
            case 3:
                lojas_tabajara()
            case 8:
                os.system('cls')
            case 9:
                print(mensagemAjuda)
            case 0:
                exit()
            case _:
                print('Escolha uma das opções indicadas')

    except ValueError:
        print(mensagemValueError)
        continue
