print('Exercício 10: Verificar o turno de estudo')
turno = input('Escreva o turno em que você estuda (M/V/N):\n')

match turno:
    case 'M':
        print('Bom dia!')
    case 'V':
        print('Boa tarde!')
    case 'N':
        print('Boa Noite!')
    case default:
        print('Valor inválido')
