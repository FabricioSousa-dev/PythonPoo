from rich import print, inspect
from classesex005 import Aluno, Professor, Funcionario
a1 = Aluno('josé',17, "Informática", "T01")
a1.Aniversario()
a1.Fazer_matricula()
#inspect(a1,methods=True)


p1 = Professor("Samuel", 37, "Biologia", "Mestre")
p1.Aniversario()
p1.Dar_aula()
#inspect(p1,methods=True)

f1 = Funcionario("Claudia", 27, "Secretária", "Secretaria")
f1.Aniversario()
f1.Bater_pontos()
#inspect(f1,methods=True)