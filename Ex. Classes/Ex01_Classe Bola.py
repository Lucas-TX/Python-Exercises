# Declara classe bola
class Bola:
    # Define construtores da classe bola:
    # Ao inicilizar o objeto
    #   Para declarar um objeto, o atributo é obrigatório
    def __init__(self, cor, material):
        # self -> para referenciar o objeto atual
        # .cor -> atributo cor
        # = cor -> argumento passado para essa função
        self.cor = cor
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        print(f'{self.cor}')

    def calcula_raio(self, circunferencia):
        if self.material == 'Plástico':
            raio = circunferencia / (2 * 3.14)
            print(f'Raio = {raio}')


# Declara objeto da classe Bola
bola_futebol = Bola('Amarelo', 'Plástico')

# Define os atributo circunferência do objeto bola_futebol
bola_futebol.calcula_raio(35)

# chama os métodos do objeto bola_futebol
bola_futebol.mostra_cor()
bola_futebol.troca_cor('Preto')
