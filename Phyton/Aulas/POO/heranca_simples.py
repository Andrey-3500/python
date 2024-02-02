class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor..")

    def __str__(self):
     return f'{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'


class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    pass

moto = motocicleta('ver', 1234, 2)
carro = carro('Branco', 4451, 4)
caminhao = caminhao('roxo', 3564, 8)

print(moto)
print(carro)
print(caminhao)
