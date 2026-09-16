from abc import ABC, abstractmethod
class BebidaQuente(ABC):

    def Preparar(self):

    def Ferver_Agua(self):
        pass

    @abstractmethod
    def Misturar(self):
        pass
    @abstractmethod
    def Servir(self):
        pass



class Cafe(BebidaQuente):

    def Misturar(self):
        pass
    def Servir(self):
        pass

class Cha(BebidaQuente):

    def Misturar(self):
        pass
    def Servir(self):
        pass

class Leite(BebidaQuente):

    def Misturar(self):
        pass
    def Servir(self):
        pass