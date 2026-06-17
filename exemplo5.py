class Alunos:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def mostrar_nota(self):
        print(f"{self.nome} Sua nota é {self.nota}")
    
    def verificar_aprovacao(self):
        if self.nota > 7:
            print("Você está aprovado(a)!")
        else:
            print("Você está reprovado(a)!")

aluno1 = Alunos("Maria", 10)
aluno1.mostrar_nota()
aluno1.verificar_aprovacao()

aluno1 = Alunos("Tobias", 5)
aluno1.mostrar_nota()
aluno1.verificar_aprovacao()
