from rich import print
from rich import inspect
class funcionario:
    #Atributos de classe
    empresa = "Curso em vídeo."


    #Atributos de instância
    def __init__(self, nome = '<Desconhecido>',setor = '<Desconhecido>', cargo = '<Desconhecido>'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}. "





f1 = funcionario("Maria", "Administração", "Diretora")
#inspect(f1,methods=True)
print(f1.apresentacao())

f2 = funcionario("Pedro", "T.I", "Programador")
print(f2.apresentacao())
#inspect(f2)