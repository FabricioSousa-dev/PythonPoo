from personagem import Guerreiro, Mago
def main():
    # Criando os personagens
    p1 = Guerreiro("Mega Man", 1000)
    p2 = Mago("Merlin", 5000)
    p3 = Guerreiro("Kratos", 1500)

    # Simulando a batalha e ações
    print("--- INÍCIO DA BATALHA ---")
    p1.atacar(p2, 200)
    p2.atacar(p1, 150)
    p3.atacar(p1, 400)

    p1.curar()
    p2.curar()
    p3.curar()

if __name__ == "__main__":
    main()