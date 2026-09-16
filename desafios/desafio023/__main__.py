from rich import print,inspect
from poligono import *



def main():
    p1 = circulo(21)

    print(f"Perimetro = {p1.Perimetro():.1f}")
    print(f"Area = {p1.Area():.1f}")


if __name__ == '__main__':
    main()