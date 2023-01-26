class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        if self.idade < 21:
            tamanho_crescimento = 0.5 * (21 - self.idade)
            self.crescer(tamanho_crescimento)
        self.idade += anos

    def crescer(self, tamanho):
        self.altura += tamanho

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso


pessoaA = Pessoa('Lucas', 15, 100, 180)
print(f'Idade: {pessoaA.idade}')
print(f'Peso: {pessoaA.peso}')
print(f'Altura: {pessoaA.altura}')

pessoaA.envelhecer(1)
pessoaA.emagrecer(10)
pessoaA.crescer(20)

print(f'Idade: {pessoaA.idade}')
print(f'Peso: {pessoaA.peso}')
print(f'Altura: {pessoaA.altura}')
