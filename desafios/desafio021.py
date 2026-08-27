from rich import print

class Caneta:
    def __init__(self,cor ="azul"):
        escolha = ''
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "Vermelho" | "vermelha":
                escolha = "[red]"
            case "Verde":
                escolha = "[green]"
            case _:
                escolha = "[White]"
        self.cor = escolha
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def quebrar_linha(self,qtd=1):
        print("\n"*qtd)


    def escrever(self,texto):
        if self.tampada == True:
            print("Tire a tampa da caneta antes!")
        else:
            print(f"{self.cor}{texto}[/]")


c1 = Caneta("Vermelha")
c1.destampar()
c1.quebrar_linha(2)
c1.escrever("Teste")