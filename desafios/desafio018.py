class churrasco:
    def __init__(self,tiltulo, quant = 0):
        self.nome = tiltulo
        self.quant = quant

    def analise(self):
        preço = 82.40
        gramas = 400
        reco = self.quant * gramas
        ct = reco * preço
        print(f"Analisando o {self.nome} com {self.quant} convidados.")
        print(f"Cada participante comera {gramas/1000}KG e cada KG custa {preço}")
        print(f"É recomendado comprar {reco}KG de carne.")
        print(f"O custo total será {ct:,.0f}")
        print("Cada pessoa pagara {}")






c1 = churrasco("Pedro", 15)
c1.analise()
#400g por pessoa
#R$82,90kg