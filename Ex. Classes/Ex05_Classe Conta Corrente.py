class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, quantia_deposito):
        self.saldo += quantia_deposito

    def saque(self, quantia_saque):
        self.saldo -= quantia_saque


contaA = ContaCorrente(numero_conta=123, nome_correntista='Lucas')

print(f'A conta {contaA.numero_conta} do cliente {contaA.nome_correntista} está com saldo = {contaA.saldo}')
contaA.alterar_nome('Lucas Teixeira')
print(f'Novo nome: {contaA.nome_correntista}')
contaA.deposito(15)
print(f'Novo saldo: {contaA.saldo}')
contaA.saque(50)
print(f'Novo saldo: {contaA.saldo}')
