class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self, quantidade_adicionada):
        self.estoque += quantidade_adicionada

    def vender(self, quantidade_venda):
        if quantidade_venda > self.estoque:
            print(f"Não há {quantidade_venda} unidades de {self.nome} para serem vendidas, apenas {self.estoque} unidades!")
        else:
            self.valor_venda = self.preco * quantidade_venda
            self.estoque -= quantidade_venda
    
    def exibir_valor(self):
        print(f"O valor da venda do produto {self.nome} foi: ")
        print(self.valor_venda)

    def exibir_estoque(self):
        print(f"A quantidade no estoque do produto {self.nome}, é {self.estoque}")
    
produto1 = Produto("Air Fryer", 250, 10)
produto1.exibir_estoque()
produto1.adicionar_estoque(10)
produto1.exibir_estoque()
produto1.vender(5)
produto1.exibir_valor()
produto1.exibir_estoque()

produto2 = Produto("Placa Solar", 10000, 10)
produto2.exibir_estoque()
produto2.adicionar_estoque(10)
produto2.exibir_estoque()
produto2.vender(30)

    

        