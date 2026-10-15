from abc import ABC, abstractmethod
from rich.console import Console
from rich.panel import Panel


class Funcionario(ABC):
    sal_min = 1_612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def Calc_sal(self):
        pass

    def Analisar_sal(self):
        console = Console()
        qtd_minimos = self.salario / self.sal_min
        tipo = type(self).__name__

        texto = (
            f"O salário de [blue]{self.nome}[/blue] "
            f"([magenta]{tipo}[/magenta]) é de "
            f"[green]R${self.salario:.2f}[/green] e corresponde a "
            f"[yellow]{qtd_minimos:.1f} salários mínimos[/yellow]."
        )

        console.print(Panel(texto, title="Análise de Salário"))


class FuncionarioHorista(Funcionario):

    def __init__(self,nome,valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas
        self.sal_bruto = self.valor_hora * self.qtd_horas

    def Calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)
        return self.salario

class FuncionarioMensalista(Funcionario):
    def __init__(self,nome,sal_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def Calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)
        return self.salario