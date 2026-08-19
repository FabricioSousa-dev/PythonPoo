class funcionario:
    def __init__(self, nome = '<Desconhecido>',setor = '<Desconhecido>', cargo = '<Desconhecido>'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa curso em vídeo. "





f1 = funcionario("Maria", "Administração", "Diretora")
print(f1.apresentacao())

f2 = funcionario("Pedro", "T.I", "Programador")
print(f2.apresentacao())