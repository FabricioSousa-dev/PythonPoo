from rich import inspect

from funcionario import *

def main():
    f1 = FuncionarioHorista("pedro", 12,200)
    inspect(f1)
    f1.Calc_sal()
    f1.Analisar_sal()

    f2 = FuncionarioMensalista("Amanda", 9500)
    f2.Calc_sal()
    f2.Analisar_sal()



if __name__ == '__main__':
    main()






