numeros = []
cont = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        cont = cont + 1
        numeros.append(c)
r = sum(numeros)
print('A soma de todos os valores solicitados é {}'.format(r))

