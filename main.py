from banco_lista import BancoLista
from conta import Conta, ContaPoupanca

if __name__ == "__main__":
    
    banco = BancoLista(taxa_juros=0.02)  # Taxa de juros de 2%

    
    conta1 = Conta("12345-6", "João", 1000)
    conta2 = ContaPoupanca("78901-2", "Maria", 2000)

    
    banco.cadastrar(conta1)
    banco.cadastrar(conta2)

    
    print("Saldo antes dos juros:", conta2.get_saldo())
    banco.render_juros("78901-2")
    print("Saldo depois dos juros:", conta2.get_saldo())

    
    banco.render_juros("12345-6")
