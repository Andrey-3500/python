def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {(nome)} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador : '))
g = str(input('gols : '))

if g.isnumeric():
    gols = int(g)

else:
    g = 0

if n.strip() == '':
    jogador(gols=g)

else:
    jogador(n, g)
