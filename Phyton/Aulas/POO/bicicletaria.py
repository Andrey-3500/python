class bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha=1):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('plim plim..')

    def parar(self):
        print('Parando bicicleta ...')
        print('Biciclera parada!')

    def acelerar(self):
        print('Vruuum ...')

    def get_cor(self):
        return self.cor

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'

b1 = bicicleta('verde', 'monark', 2000, 150)

bicicleta.buzinar(b1)
print(b1.cor)

b2 = bicicleta('vermelha', 'caloi', 2022, 500)
b2.buzinar()
b2.parar()
b2.acelerar()
print(b2.cor, b2.modelo, b2.ano, b2.valor)
print(b1.__str__())