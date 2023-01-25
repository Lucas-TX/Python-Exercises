from tabulate import tabulate
print('Exercício 43')

head_tabela_Produtos = ['Especificação', 'Código', 'Preço']
tabela_produtos = (
    ["Cachorro quente", 100, 1.20],
    ["Bauru Simples", 101, 1.30],
    ["Bauru com ovo", 102, 1.50],
    ["Hambúrguer", 103, 1.20],
    ["Cheeseburguer", 104, 1.30],
    ["Refrigerante", 105, 1.00],
)
head_pedido = ['Produto', 'Quantidade', 'Preço unitário', 'Preço total']
tabela_pedido = []
print('---- Tabela de produtos -----')
print('\n')
print(tabulate(tabela_produtos, headers=head_tabela_Produtos))
print('\n')
print('Iniciando caixa Registradora')
print('Digite 0 para concluir o pedido')
print('\n')

valor_totalCompra = 0
while True:
    contador_validaCodigoPedido = 0

    try:
        codigo_pedido = int(input('Código do Produto: '))
        qtd_pedida = int(input('Quantidade solicitada: '))
    except ValueError:
        print('Número inválido. Escreva um número inteiro')
        continue
    if codigo_pedido == 0 or qtd_pedida == 0:
        break

    for row in tabela_produtos:
        especificao_Produto = row[0]
        codigo_produto = row[1]
        preco_produto = row[2]
        if codigo_pedido == codigo_produto:
            valor_Total = preco_produto * qtd_pedida
            tabela_pedido.append([especificao_Produto, qtd_pedida, preco_produto, valor_Total])
            valor_totalCompra += valor_Total
            break
        contador_validaCodigoPedido += 1
    if contador_validaCodigoPedido == len(tabela_produtos):
        print('Código inválido. Escolha um dos códigos tabela acima')

print("---- Pedido Final ----")
tabela_pedido.append(['Total', '-', '-', valor_totalCompra])
print(tabulate(tabela_pedido, headers=head_pedido))
