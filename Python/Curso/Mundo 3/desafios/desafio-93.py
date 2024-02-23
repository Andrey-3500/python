jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantidade de patidas que {jogador["nome"]} jogou: '))

for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele fez na {p+1}° partida: ')))
print('-'*50)
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print(jogador)
print('-'*50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*50)
print(f'O jogador {jogador["nome"]} jogo {len(gols)} partidas.')

for p, g in enumerate(gols):
    print(f'-> Na {p+1}° partida, fez {g} gols. ')
print(f'Foi um total de {jogador["total"]} gols.')