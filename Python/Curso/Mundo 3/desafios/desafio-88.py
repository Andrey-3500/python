from random import randint
from time import sleep
lista = []
jogos = []
quantidade = int(input('quantos jogos gostaria de gerar ? >> '))

tot = 1
while tot <= quantidade:
    cont = 0
    while True:
        valor = randint(1, 60)
        if valor not in lista:
            lista.append(valor)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(0.5)
