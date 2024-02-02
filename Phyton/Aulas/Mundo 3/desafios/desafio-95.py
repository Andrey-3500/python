jogador = {}
time = []
gols = []
while True:
    print('-'*50)
    jogador['nome'] = str(input('Nome do jogador: '))

    partidas = int(input(f'Quantidade de patidas que {jogador["nome"]} jogou: '))

    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols ele fez na {p+1}° partida: ')))
    print('-'*50)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    time.append(jogador.copy())
    gols.clear()

    while True:
        resp = str(input('Quer continuar? [S/N]\n >>')).upper().split()[0]

        if resp in 'SN':
            break
        else:
            print('Erro! Responda com S ou N')

    if resp == 'N':
        break

print('-'*50)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')

print()
print('-'*50)

for k, v in enumerate(time):

    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:

    dados = int(input('Mostrar dados de qual jogador (999 parar) : '))

    if dados == 999:
        break

    if dados >= len(time):
        print(f'ERRO ! Não existe jogador com o código {dados}!')

    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}')

        for j, g in enumerate(time[dados]['gols']):
            print(f'-> No jogo {j+1}° fez {g} gols.')

print('-'*50)
print(f'{"Volte Sempre !":^50}')
print('-'*50)