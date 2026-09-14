from abc import ABC, abstractclassmethod, abstractmethod  # Abstract base classes
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass



class Aluno(Pessoa):

    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def Fazer_matricula(self):
        print(f"O {self.nome} acabou de fazer a matricula!")

    def estudar(self):
        print(f"{self.nome} está estudando na turma {self.turma} matriculado no curso {self.curso}")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def Dar_aula(self):
        print(f"O prof {self.nome} começou a dar aula!")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade}  no {self.nivel}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def Bater_pontos(self):
        print(f"O {self.nome} acabou de bater ponto!")

    def estudar(self):
        print(f"{self.nome} se especializa para a área de {self.setor}!")
