from rich import print
from rich.panel import Panel
class ControleRemoto:

    canal_max:int = 5
    canal_min:int = 1
    volum_minimo:int = 1
    volum_minimo_max:int = 10

    def __init__(self,canal = 1,volum = 1):
        self.canal_atual:int = canal
        self.volume_atual:int = volum
        self.ligado:bool = False

    def ligar_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        pass

    def canal_menos(self):
        pass

    def volume_mais(self):
        pass

    def volume_menos(self):
        pass

    def mostrar_tv(self):
        conteudo = ''
        if  not self.ligado:
            conteudo = f":prohibited: [red]A tv está desligada![/red]"
        else:
            conteudo = f"CANAL = "
            for canal in range(ControleRemoto.canal_min,ControleRemoto.canal_max+1):
                if canal == self.canal_atual:
                    conteudo += (f" [yellow on yellow] {canal} [/]")
                else:
                    conteudo += (f" {canal} ")
            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.canal_min,ControleRemoto.canal_max+1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan].[/]"
                else:
                    conteudo += "[black on white].[/]"

        tv = Panel(conteudo,title = '[TV]',width=40)
        print(tv)


c1 = ControleRemoto(2,5)
c1.ligar_desliga()
c1.mostrar_tv()