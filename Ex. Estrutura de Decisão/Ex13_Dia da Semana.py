print('Exercício 13: Dia da semana')
dia_numero = int(input('Insira um número correspondente ao dia da semana:\n'))
match dia_numero:
    case 1:
        print(f'O dia da semana é Domingo')
    case 2:
        print(f'O dia da semana é Segunda-Feira')
    case 3:
        print(f'O dia da semana é Terça-Feira')
    case 4:
        print(f'O dia da semana é Quarta-Feira')
    case 5:
        print(f'O dia da semana é Quinta-Feira')
    case 6:
        print(f'O dia da semana é Sexta-Feira')
    case 7:
        print(f'O dia da semana é Sábado')
    case _:
        print(f'Valor inválido')
