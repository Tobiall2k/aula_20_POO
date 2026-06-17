class Conta:
    def __init__(self, nome_titular, saldo_conta):
        self.nome = nome_titular
        self.saldo = saldo_conta
    
    def depositar(self, depositar):
        self.saldo += depositar
    
    def sacar(self, saque):
        if self.saldo <= 0:
            print(f"{self.nome} você está sem saldo ou com saldo negativo, por isso não pode sacar nenhum valor!")
        elif saque > self.saldo:
            print(f"{self.nome} O valor que você deseja sacar é maior que o seu saldo!")
        else:
            self.saldo -= saque
    
    def exibir_saldo(self):
        print("\n")
        print(f"{self.nome} seu saldo atual é: ")
        print(self.saldo)
        print("\n")

conta_1 = Conta("Tobias", 1600)
conta_1.exibir_saldo()
conta_1.depositar(200)
conta_1.exibir_saldo()
conta_1.sacar(100)
conta_1.exibir_saldo()

conta_2 = Conta("Lucas", 100)
conta_2.exibir_saldo()
conta_2.depositar(700)
conta_2.exibir_saldo()
conta_2.sacar(1000)

conta_3 = Conta("Samuel", 0)
conta_3.exibir_saldo()
conta_3.sacar(100)


    
        
    