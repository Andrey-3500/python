from random import randint
numeros = []
def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for x in range(0, 5):

        v = randint(0, 10)
        print(v, end=' ')
        numeros.append(v)
        x += 1
    print()

def somapar():
    spar = 0
    print(f'Somando os valores pares de {numeros}, temos ',end='')
    for v in (numeros):
        if v % 2 == 0:
            spar += v
    print(spar)


sorteia()
somapar()
