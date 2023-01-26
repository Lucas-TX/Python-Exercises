class Tv:
    def __init__(self, volume=0, canal=0):
        self.volume = volume
        self.canal = canal

    def alterar_canal(self, novo_canal):
        if novo_canal < 0:
            print("Não é possível selecionar um canal negativo")
        else:
            self.canal = novo_canal

    def alterar_volume(self, valor):
        novo_volume = self.volume + valor
        if novo_volume < 0:
            print("Não é possível selecionar um volume negativo")
        else:
            self.volume = novo_volume


tv_A = Tv()
print(f'Volume - {tv_A.volume}')
print(f'Canal - {tv_A.canal}')
tv_A.alterar_canal(12)
tv_A.alterar_volume(80)
tv_A.alterar_volume(-70)
print(f'Volume - {tv_A.volume}')
print(f'Canal - {tv_A.canal}')
