from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

j = int(input('Qual a sua jogada? '))
comp = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('---'*11)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[j]))
print('---'*11)

if comp == 0:

    if j == 0:
        print('EMPATE')
    elif j == 1:
        print('JOGADOR VENCEU!')
    elif j == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada invalida!')

elif comp == 1:

    if j == 0:
        print('COMPUTADOR VENCEU!')
    elif j == 1:
        print('EMPATE')
    elif j == 2:
        print('JOGADOR VENCEU!')
    else:
        print('Jogada invalida!')

elif comp == 2:

    if j == 0:
        print('JOGADOR VENCEU!')
    elif j == 1:
        print('COMPUTADOR VENCEU!')
    elif j == 2:
        print('EMPATE')
    else:
        print('Jogada invalida!')