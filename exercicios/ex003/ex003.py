class Contabancaria:
    '''
Cria uma conta bancaria e permite saques e depositos
    '''
    def __init__(self,nome = "<Desconhecido>", saldo = 0, id = 0 ):
        self.Titular = nome
        self.saldo = saldo
        self.id = id
        print(f"Conta {self.id} de titular {self.Titular} criada com sucesso, saldo atual: R${self.saldo:,.2f}")

    def __str__(self):
        return f' A conta {self.id} de {self.Titular} tem R${self.saldo:,.2f} de saldo.'

    def depositar(self,valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self,valor):
        if valor > self.saldo:
            print(f"Saldo de R${valor:,.2f} bloqueado ao conta {self.id}")
        else:
            self.saldo -= valor
            print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}")


c1 = Contabancaria("Carlos",1500,122)
c1.depositar(1500)
c1.sacar(10000000000000000)
print(c1)
