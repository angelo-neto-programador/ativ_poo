from conta import Conta, ContaPoupanca

class BancoLista:
    def __init__(self, taxa_juros=0.01):  # Taxa de juros padrão de 1%
        self.contas = []  
        self.taxa_juros = taxa_juros

    def cadastrar(self, conta: Conta):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta Inexistente!")

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta Inexistente!")

    def render_juros(self, numero):
       
        conta = self.procurar_conta(numero)
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(self.taxa_juros)
        else:
            print("A conta fornecida não é uma poupança ou não existe!")
