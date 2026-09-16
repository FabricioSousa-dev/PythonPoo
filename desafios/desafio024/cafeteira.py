from abc import ABC, abstractmethod
class BebidaQuente(ABC):


    def Preparar(self):
        print("-- Iniciando o prepararo --")
        self.Ferver_Agua()
        self.Misturar()
        self.Servir()
        print("-- Bebida pronta --")

    def Ferver_Agua(self):
        print("1 - Fervendo água a 100 graus Celsius.")

    @abstractmethod
    def Misturar(self):
        pass
    @abstractmethod
    def Servir(self):
        pass



class Cafe(BebidaQuente):

    def Misturar(self):
        print("2 - A passar a agua quente pelo po de cafe moido.")

    def Servir(self):
        print("3 - Servindo em xícara de chá pequena.")

class Cha(BebidaQuente):

    def Misturar(self):
        print("2 - Mergulhando o sachê de ervas na água.")

    def Servir(self):
        print("3 - Servindo na caneta de porcelana com limão.")

class Leite(BebidaQuente):

    def Misturar(self):
        print("2 - Passando o vapor pressurizado do leite.")

    def Servir(self):
        print("3 - Servindo em caneca grande, já com café.")