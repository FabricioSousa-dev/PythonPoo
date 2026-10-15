from abc import ABC, abstractmethod
import random
from rich import print  # Opcional (usado para formatação com cores no vídeo)

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    @abstractmethod
    def curar(self):
        pass

    def receber_dano(self, dano):
        # Simula a rolagem de dados do RPG (dano de 0 até o valor informado)
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"[red]{self.nome} recebeu um dano de {fator} (Vida atual: {self.vida})[/red]")

    def atacar(self, alvo, forca=100):
        if self.vida > 0 and alvo.vida > 0:
            # Sorteia um dos golpes da lista
            golpe = random.choice(self.golpes)
            print(f"[green]{self.nome}[/green] atacou [red]{alvo.nome}[/red] com um [blue]{golpe}[/blue]!")
            # O alvo recebe o dano proporcional à força máxima informada
            alvo.receber_dano(forca)
        else:
            print("[yellow]O ataque não pode acontecer porque um dos personagens está sem vida![/yellow]")


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Golpe de Machado', 'Pulo Giratório']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome} (Guerreiro) enrolou uma atadura nos ferimentos e recuperou {fator} pontos de vida![/blue]")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Raio de Luz', 'Magia Estática']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[magenta]{self.nome} (Mago) fez uma magia de cura e recuperou {fator} pontos de vida![/magenta]")