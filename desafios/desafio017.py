class produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        print("=-="*20)
        print(self.nome.center(20))
        print("=-="*20)
        print(f"R${self.valor:,.2f}")


p1 = produto("Iphone pro max",2000)
p2 = produto("Iphone pro min",1000)

p1.etiqueta()
p2.etiqueta()