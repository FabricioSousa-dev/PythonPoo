from rich import print
from time import sleep
class Livro:
    def __init__(self,titulo,paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1


        print(f":open_book: você acabou de abrir o livro {self.titulo} que tem {self.total_paginas} páginas no total e você agora está na página {self.pagina_atual}")



    def avancar_paginas(self,qtd = 1):
        cont = 0
        for pg in range(0,qtd,1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"pág{self.pagina_atual} :arrow_foward:",end="")
                sleep(0.2)
                cont += 1
        print(f"[blue]você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][/blue]")
        if self.fim_do_livro():
            print(f":closed_book: [red]você chegou ao final do livro {self.titulo}[/red]")



    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False


l1 = Livro("Teste1",20)
l1.avancar_paginas(3)
l1.avancar_paginas(30)

