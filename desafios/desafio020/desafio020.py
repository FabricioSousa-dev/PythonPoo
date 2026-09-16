from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()


    def add_favorito(self,fav):
        self.favoritos.append(fav)
        self.favoritos = sorted(self.favoritos,key=str.lower)

    def ficha(self):
        conteudo = ''
        conteudo += f"Nome real: [black on blue] {self.nome} [/] "
        conteudo += f"\nJogos favoritos::"
        for num,fav in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{fav}[/]"
        painel = Panel(conteudo,title=f"jogador <{self.nick}", width=40)
        print(painel)



j1 = Gamer("Fabricio","Kiritsugo")
j1.add_favorito("Metal gear solid 3")
j1.ficha()