from rich import print
from rich.panel import Panel
class produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-'* 30}"
        preçof = f"R${self.valor:,.2f}"
        conteudo += f"{preçof.center(30, '.')}"
        etiqueta = Panel(conteudo,title="Produto", width=34)
        print(etiqueta)



p1 = produto("Iphone pro max",2_000)
p2 = produto("Iphone pro min",1_000)

p1.etiqueta()
p2.etiqueta()