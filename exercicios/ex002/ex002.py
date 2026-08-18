#Declaração da classe.
class Gafanhoto:
    '''
Essa classe cria um gafanhoto, que é uma pessoa que tem nome é idade
Para criar um nova pessoa, use
variavel = gafanhoto(nome, idade)
    '''
    def __init__(self,nome = 'vazio' , idade = 0): #Metado construtor
        #Atributos de instância.
        self.nome = nome
        self.idade = idade

    #Metodos de instância
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) tem {self.idade} anos"




#Declaração do objetos.
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
#print(g1.mensagem())

print(g1.__doc__)# Dunder attribute