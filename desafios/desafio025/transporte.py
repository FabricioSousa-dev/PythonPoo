from abc import ABC,abstractmethod
from typing import Any


class Transporte(ABC):

    def __init__(self,distancia,peso):
        self.distancia = distancia
        self.peso = peso
        self.frete = 0



    @abstractmethod
    def Calc_frete(self):
        pass


class Moto(Transporte):
    fator: float = 0.50
    taxa_peso: float = 2.00
    def __init__(self,distancia):
        super().__init__(distancia)

    def Calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return (f"R$ {self.frete:.2f}")


class Caminhao(Transporte):
    fator: float = 1.20
    def __init__(self,distancia,peso):
        super().__init__(distancia,peso)

    def Calc_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return "Só realizamos entrega de caminhão acima de 50 KM."
        else:
            self.frete = self.distancia * Caminhao.fator
            return (f"R$ {self.frete:.2f}")


class Drone(Transporte):
    fator: float = 9.50
    def __init__(self,distancia):
        super().__init__(distancia)

    def Calc_frete(self):
        if self.distancia <=10:
            self.frete = self.distancia * Drone.fator
            return (f"R$ {self.frete:.2f}")
        else:
            self.frete = 0
            return "Não realizamos entrega de drone a essa distãncia."
