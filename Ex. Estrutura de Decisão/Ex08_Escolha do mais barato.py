print('Exercício 8: Escolha o mais barato entre 3')
dict_produtos = {}
preco1 = input('Insira o preço do primeiro produto:\n')
dict_produtos["Produto 1"] = float(preco1)
preco2 = input('Insira o preço do segundo produto:\n')
dict_produtos["Produto 2"] = float(preco2)
preco3 = input('Insira o preço do terceiro produto:\n')
dict_produtos["Produto 3"] = float(preco3)

menorPreco = list(dict_produtos.values())[0]
nome_produto = list(dict_produtos.keys())[0]

for produto, preco in dict_produtos.items():
    if preco < menorPreco:
        menorPreco = preco
        nome_produto = produto
print('O produto', nome_produto, 'é o de menor preço (R$', menorPreco, ').')
