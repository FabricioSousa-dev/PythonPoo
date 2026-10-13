from rich import print,inspect
from rich.table import Table
from transporte import *

def main():
    dist = 100

    viagem = [Moto(dist),Caminhao(dist,2.6),Drone(dist)]

    """entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}KM = {entrega.Calc_frete()}")"""

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(f"{dist}KM", f"{type(item).__name__}", f"{item.Calc_frete()}")

    print(tabela)







if __name__ == '__main__':
    main()
