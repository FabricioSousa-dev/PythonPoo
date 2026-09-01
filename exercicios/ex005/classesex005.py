class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def Fazer_matricula(self):
        print(f"O {self.nome} acabou de fazer a matricula!")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def Dar_aula(self):
        print(f"O prof {self.nome} começou a dar aula!")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def Bater_pontos(self):
        print(f"O {self.nome} acabou de bater ponto!")
