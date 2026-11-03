class Contabancaria:
    '''
    Cria uma conta bancaria e permite saques e depositos
    '''
    def __init__(self,nome = "<Desconhecido>", saldo = 0, id = 0 ):
        self._Titular = nome
        self.__saldo = saldo
        self.id = id #publico (+)
        print(f"Conta {self.id} de titular {self._Titular} criada com sucesso, __saldo atual: R${self.__saldo:,.2f}")

    def __str__(self):
        #return f' A conta {self.id} de {self._Titular} tem R${self.__saldo:,.2f} de __saldo.'
         return f"O estado da conta: {self.__dict__}"

    def depositar(self,valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self,valor):
        if valor > self.__saldo:
            print(f"Saldo de R${valor:,.2f} bloqueado ao conta {self.id}")
        else:
            self.__saldo -= valor
            print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}")

