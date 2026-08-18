#Declaração da classe.
class Gafanhoto:
    def __init__(self): #Metado construtor
        #Atributos de instância.
        self.nome = ''
        self.idade = 0

    #Metodos de instância
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"{self.nome} é gafanhoto tem {self.idade} anos"




#Declaração do objetos.
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 20
g1.aniversario()
print(g1.mensagem())


g2 = Gafanhoto()
g2.nome = "Julian"
g2.idade = 23
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())