class Conta:
    def __init__(self, nome, cpf, numero, saldo=0.0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def imprimir_saldo(self):
        print(f"Conta: {self.numero} | Titular: {self.nome} | Saldo: R$ {self.saldo:.2f}")


# Exemplo de uso
conta1 = Conta("João", "123.456.789-00", "001234", 500.0)
conta1.imprimir_saldo()
conta1.depositar(200)
conta1.sacar(100)
conta1.imprimir_saldo()
conta1.sacar(700)