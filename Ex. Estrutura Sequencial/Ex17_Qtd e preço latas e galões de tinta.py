print('Exercício 17: Calcula a quantidade de tinta necessária e o preço total')
str_areaTotal = input('Escreva o tamanho da área, em metros quadrados, em que deseja-se pintar:\n')
float_quantidadeLitrosTinta = float(str_areaTotal)/6
print('Para ', str_areaTotal, ' metros quadrados, é necessário ', round(float_quantidadeLitrosTinta, 2),
      ' litros de tinta.')

# Análise da quantidade de latas necessárias
float_quantidadeLatasTinta = float_quantidadeLitrosTinta/18
float_restoDivisaoQuantidadeLatasTinta = float_quantidadeLitrosTinta % 18
if float_restoDivisaoQuantidadeLatasTinta != 0:
    print('Para comprar apenas latas (18 litros), compre ', int(float_quantidadeLatasTinta) + 1, ' lata(s) de tinta')
    print('O valor total será R$', (int(float_quantidadeLatasTinta)+1) * 80)
else:
    print('Para comprar apenas latas (18 litros), compre ', int(float_quantidadeLatasTinta), ' lata(s) de tinta')
    print('O valor total será R$', int(float_quantidadeLatasTinta) * 80)

# Análise da quantidade de galões necessários
float_quantidadeGalaoTinta = float_quantidadeLitrosTinta/3.6
float_restoDivisaoQuantidadeGalaoTinta = float_quantidadeLitrosTinta % 3.6
if float_restoDivisaoQuantidadeGalaoTinta != 0:
    print('Para comprar apenas galões (3,6 litros), compre ', int(float_quantidadeGalaoTinta) + 1,
          ' galão(es) de tinta')
    print('O valor total será R$', (int(float_quantidadeGalaoTinta)+1) * 25)
else:
    print('Para comprar apenas galões (3,6 litros), compre ', int(float_quantidadeGalaoTinta), ' galão(es) de tinta')
    print('O valor total será R$', int(float_quantidadeGalaoTinta) * 25)

# Análise com menor disperdício de tinta
float_quantidadeLitrosTinta = float_quantidadeLitrosTinta * 1.1
print('Considerando 10% de folga na quantidade de tinta, necessita-se de ', round(float_quantidadeLitrosTinta, 2),
      ' litros de tinta')
int_quantidadeLatasTinta = int(float_quantidadeLitrosTinta / 18)
float_restoDivisaoQuantidadeLatasTinta = float_quantidadeLitrosTinta % 18

if float_restoDivisaoQuantidadeLatasTinta == 0:
    print('Para minimizar o disperdício, deve-se comprar ', int_quantidadeLatasTinta, ' lata(s) de tinta')
elif float_restoDivisaoQuantidadeLatasTinta > 16.2:
    print('Para minimizar o disperdício, deve-se comprar ', int_quantidadeLatasTinta + 1, ' lata(s) de tinta')
else:  # O resto da divisão estará entre 0 e 16.2
    float_quantidadeLitrosTinta = float_restoDivisaoQuantidadeLatasTinta
    int_quantidadeGalaoTinta = int(float_quantidadeLitrosTinta / 3.6)
    float_restoDivisaoQuantidadeGalaoTinta = float_quantidadeLitrosTinta % 3.6

    if float_restoDivisaoQuantidadeGalaoTinta == 0:
        print('Para minimizar o disperdício, deve-se comprar ', int_quantidadeLatasTinta, ' latas de tinta e',
              int_quantidadeGalaoTinta, ' Galão (es) de tinta.')
        print('O valor total dessa compra será R$', (int_quantidadeLatasTinta*80) + (int_quantidadeGalaoTinta*25))
    else:
        print('Para minimizar o disperdício, deve-se comprar ', int_quantidadeLatasTinta, ' latas de tinta e',
              int_quantidadeGalaoTinta + 1, ' Galão(es) de tinta.')
        print('O valor total será R$', (int_quantidadeLatasTinta * 80) + ((int_quantidadeGalaoTinta + 1)*25))
