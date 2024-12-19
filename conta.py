class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def get_numero(self):
        return self.numero

    def creditar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido para depósito!")

    def debitar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido!")

    def get_saldo(self):
        return self.saldo


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0):
        super().__init__(numero, titular, saldo)

    def render_juros(self, taxa):
        
        if taxa > 0:
            juros = self.saldo * taxa
            self.creditar(juros)
        else:
            print("Taxa de juros inválida!")
