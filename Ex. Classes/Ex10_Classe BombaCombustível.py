class BombaCombustivel:
    def __init__(self, tipo_combutivel, valor_litro, qtd_combustivel):
        self.tipo_combutivel = tipo_combutivel
        self.valor_litro = valor_litro
        self.qtd_combustivel = qtd_combustivel

    def abastecer_por_valor(self, valor_pago):
        litros = round(valor_pago / self.valor_litro, 2)
        if self.qtd_combustivel - litros < self.retorna_qtd_combustivel():
            return Exception('Não há combustível suficiente para abastercer')
        self.qtd_combustivel -= litros
        print(f'O carro será abastecido com {litros} litros de {self.tipo_combutivel}')

    def abastecer_por_litro(self, litros):
        valor_pago = round(litros * self.valor_litro, 2)
        if self.qtd_combustivel - litros < self.retorna_qtd_combustivel():
            return Exception('Não há combustível suficiente para abastercer')
        self.qtd_combustivel -= litros
        print(f'O cliente deve pagar R${valor_pago}')

    def altera_valor_por_litro(self, novo_valor):
        if novo_valor <= 0:
            print('Não é possível inserir um valor negativo')
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combutivel = novo_combustivel

    def alterar_qtd_combustivel(self, nova_quantidade):
        if nova_quantidade < 0:
            print('Não é possível inserir uma quantidade negativa.')
        else:
            self.qtd_combustivel = nova_quantidade

    def retorna_qtd_combustivel(self):
        return self.qtd_combustivel


bomba_sul = BombaCombustivel(tipo_combutivel='Gasolina', valor_litro=6.50, qtd_combustivel=100)
bomba_sul.abastecer_por_litro(150)
print(bomba_sul.retorna_qtd_combustivel())
bomba_sul.abastecer_por_valor(50)
print(bomba_sul.retorna_qtd_combustivel())
