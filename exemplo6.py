class Celular:
    def __init__(self, marca, modelo, bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
    
    def ligar(self):
        if self.bateria < 10  and self.bateria > 0:
            faltando = 0 + self.bateria
            self.bateria -= faltando
        elif self.bateria > 0:
            self.bateria -= 10
    
    def carregar(self):
        if self.bateria < 100:
            self.bateria += 10
        elif self.bateria > 90:
            faltando = 100 - self.bateria
            self.bateria += faltando
        

    def exibir_bateria(self):
        print("Sua bateria é: ")
        print(self.bateria)

celular1 = Celular("Apple", "Iphone 17 Pro Max", 50)
celular1.ligar()
celular1.exibir_bateria()
celular1.ligar()
celular1.exibir_bateria()
celular1.ligar()
celular1.exibir_bateria()
celular1.ligar()
celular1.exibir_bateria()
celular1.ligar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()
celular1.carregar()
celular1.exibir_bateria()

    
      