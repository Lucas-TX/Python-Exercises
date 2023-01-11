print('Exercício 16: Calcula a quantidade de latas de tinta necessárias e o preço total')
str_areaTotal = input('Escreva o tamanho da área, em metros quadrados, em que deseja-se pintar:\n')
float_quantidadeLitrosTinta = float(str_areaTotal)/3
print('Para ', str_areaTotal, ' metros quadrados, é necessário ', round(float_quantidadeLitrosTinta, 2), ' litros de tinta.')

# Análise da quantidade de latas necessárias
float_quantidadeLatasTinta = float_quantidadeLitrosTinta/18
float_restoDivisaoQuantidadeLatasTinta = float_quantidadeLitrosTinta % 18
if float_restoDivisaoQuantidadeLatasTinta != 0:
    print('Para comprar apenas latas (18 litros), compre ', int(float_quantidadeLatasTinta) + 1, ' lata(s) de tinta')
    print('O valor total será R$', (int(float_quantidadeLatasTinta)+1) * 80)
else:
    print('Para comprar apenas latas (18 litros), compre ', int(float_quantidadeLatasTinta), ' lata(s) de tinta')
    print('O valor total será R$', int(float_quantidadeLatasTinta) * 80)
