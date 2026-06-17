class Celular:
    def __init__(self, marca, modelo, bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
    
    def ligar(self):
        if self.bateria > 0 :
            self.bateria -= 10
        else:
            print("Você está sem bateria!")
    
    def carregar(self):
        if self.bateria < 100:
            faltando = 100 - self.bateria
            self.bateria += faltando

        else:
            print("Seu celular está carregado em 100%")

celular1 = ("Apple", "Iphone 17 Pro Max", 50)
    
      