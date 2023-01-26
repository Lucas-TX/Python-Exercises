class Quadrado:
    def __init__(self, tamanholado):
        self.tamanholado = tamanholado

    def muda_valor_lado(self, novo_lado):
        self.tamanholado = novo_lado

    def mostra_lado(self):
        return self.tamanholado

    def calcula_area(self) -> int:
        area = self.tamanholado ** 2
        return area


quadrado1 = Quadrado(2)
print(quadrado1.mostra_lado())
quadrado1.muda_valor_lado(4)
print(quadrado1.mostra_lado())
area_quadrado1 = quadrado1.calcula_area()
print(area_quadrado1)
