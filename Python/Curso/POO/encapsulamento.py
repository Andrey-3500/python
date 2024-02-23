class conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia


    def depositar(self, valor):
        self._saldo += valor


    def sacar(self, valor):
        self._saldo -= valor


conta = conta(1200, 100)
print(conta._saldo)
print(conta.nro_agencia)