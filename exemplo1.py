class Pessoa:
    def __init__(self, nome_digitado, idade_digitada):
        self.nome = nome_digitado
        self.idade = idade_digitada
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} | Idade: {self.idade} ")
    
    def fazer_aniversario(self):
        self.idade +=1 
    
    def verificar_idade(self):
        if self.idade < 18:
            print("Menor de idade")
        else:
            print("Maior de idade")
    
pessoa1 = Pessoa("Tobias", 16)
pessoa1.apresentar()
pessoa1.fazer_aniversario()
pessoa1.apresentar()

pessoa2 = Pessoa("Maria", 15)
pessoa2.apresentar()
