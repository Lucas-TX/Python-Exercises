class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_base(self, nova_base):
        self.base = nova_base

    def mudar_altura(self, nova_altura):
        self.base = nova_altura

    def mostra_base_retangulo(self):
        return self.base

    def mostra_altura_retangulo(self):
        return self.altura

    def calcula_area_retangulo(self):
        return self.base * self.altura

    def calcula_perimetro_retangulo(self):
        return (self.base * 2) + (self.altura * 2)


print('Exercício 3 - Classe retângulo')

while True:
    try:
        ladoA = float(input('Informe um dos lados do local: '))
        ladoB = float(input('Informe o outro lado do local: '))
        break
    except ValueError:
        print('Valor inválido')

local = Retangulo(ladoA, ladoB)
print(f'A área do local é {local.calcula_area_retangulo()}')
print(f'O perímetro do local é {local.calcula_perimetro_retangulo()}')
