from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, Qtd_lados) -> None:
        self.Qtd_lados = Qtd_lados

    @abstractmethod
    def Perimetro(self):
        pass

    @abstractmethod
    def Area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(Qtd_lados=4)
        self.lado = lado

    def Perimetro(self):
        return 4 * self.lado

    def Area(self):
        return self.lado ** 2


class circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(Qtd_lados=0)
        self.raio = raio

    def Perimetro(self):
        return 2 * math.pi * self.raio

    def Area(self):
        return math.pi * (self.raio ** 2)