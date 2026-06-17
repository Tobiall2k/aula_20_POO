class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    
    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade = 0
    
    def exibir_velocidade(self):
        print(f"Seu carro {self.marca} {self.modelo} está a uma velocidade de {self.velocidade}Km/h")

carro_1 = Carro("Chevrolet", "Camaro", 160)
carro_1.exibir_velocidade()
carro_1.acelerar()
carro_1.exibir_velocidade()
carro_1.frear()
carro_1.exibir_velocidade()

carro_2 = Carro("Ford", "Maverick", 120)
carro_2.exibir_velocidade()
carro_2.acelerar()
carro_2.exibir_velocidade()
carro_2.frear()
carro_2.exibir_velocidade()