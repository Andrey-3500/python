from random import randint
print('---'*20)
print('Vou pensar em um número entre 0 e 10. Tente Adivinhar...')
print('---'*20)

tentativas = 1
nj = 11
nc = randint(0, 10)

while nj != nc:
    nj = int(input('Em que número eu pensei? \n >> '))

    print('PROCESSANDO...')

    if nj < nc:
        print('Mais.. tente Tente novamente! ')
        tentativas += 1

    elif nj > nc:
        print('Menos.. tente Tente novamente! ')
        tentativas += 1

    elif nj == nc:
        print('PARABÉNS! Você conseguiu!')
        print('Você preciso de {} tentativas para acertar'.format(tentativas))

