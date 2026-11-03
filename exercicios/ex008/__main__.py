from ex008 import *
def main():
    c1 = Contabancaria("Maria", 5_000, 111)
    c1.depositar(500)
    c1.sacar(100)

    c1._Titular = 'Pedro' # Ele deixa, mas não mexa pois "adultos estão consetindo..."

    c1._Contabancaria__saldo = 0

    print(c1)


if __name__ == '__main__':
    main()