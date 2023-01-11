print('Exercício 13: Calcula excesso do peso de peixes e o valor da multa')
pesoTotal_peixes = input('Escreva o peso total de peixes(Kg):\n')
print('A quantidade de peixes capturados foi ', pesoTotal_peixes, ' Kg.')
if float(pesoTotal_peixes) > 50:
    excedente = float(pesoTotal_peixes)-50
    multa = excedente*4
    print('O limite estabelecido pelo regulamento de pesca foi ultrapassado em ', round(excedente, 3), ' Kg.')
    print('A multa será de R$', round(multa, 3))
elif float(pesoTotal_peixes) == 50:
    print('O peso dos peixes capturados é igual ao limite estabelecido pelo regulamento de pesca.')
    print('Nenhuma multa será gerada')
else:
    print('O peso dos peixes capturados é menor do que limite estabelecido pelo regulamento de pesca.')
    print('Nenhuma multa será gerada')
