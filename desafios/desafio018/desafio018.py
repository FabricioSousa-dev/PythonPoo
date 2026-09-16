from rich import print
from rich.panel import Panel
class churrasco:
    #Atributos de classe
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    def __init__(self,titulo,quant):
        #Atributos de instância
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.participantes} pessoas participando"


    def analisar(self):
        conteudo = f"Analisando [grenn]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
        conteudo += f"\ncada participante comerá {churrasco.consumo_padrao}KG e cada Kg custa R${churrasco.preco_kg}"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_quant_carne():,.3f}KG[/] de carne"
        conteudo += f"\nO custo total será de R${self.calcular_custo_total():.2f}"
        conteudo += f"\nCada pessoa pagará R${self.calcular_custo_individual():,.2f} para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)
    def calcular_quant_carne(self) -> float:
        return self.participantes * churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_quant_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes







c1 = churrasco("Churras da rapaziada", 15)
c1.analisar()
#400g por pessoa
#R$82,90kg