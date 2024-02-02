from random import randint
from time import sleep
jogador = {}
ranking = []
print('Valores sorteados:')
for j in range(1, 5):

    tot = len(ranking)
    jogador[f'jogador'] = f'jogador{j}'
    jogador[f'dados'] = randint(1, 6)
    sleep(0.5)
    print(f'O jogador {j} tirou {jogador["dados"]}')

    if j == 1:
        ranking.append(jogador.copy())
    else:
        if jogador['dados'] >= ranking[0]['dados']:
            ranking.insert(0, jogador.copy())

        elif jogador['dados'] <= ranking[tot-1]['dados']:
            ranking.append(jogador.copy())

        else:
            for p, v in enumerate(ranking):
                if ranking[p]['dados'] > jogador['dados'] > ranking[p+1]['dados']:
                    ranking.insert(p+1, jogador.copy())

    jogador.clear()
print()
print('Ranking do jogares')
for l in range(0, 4):
    sleep(0.5)
    print(f'{l+1}º lugar: {ranking[l]["jogador"]} com {ranking[l]["dados"]}')