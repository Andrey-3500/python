pessoas = []
temp = []
pesomaior = pesomenor = 0
while True:

    temp.append(str(input('Digite um nome: ')))
    temp.append(float(input('Digite um peso: ')))

    if len(pessoas) == 0:
        pesomaior = pesomenor = temp[1]
    else:
        if temp[1] < pesomenor:
            pesomenor = temp[1]

        elif temp[1] > pesomaior:
            pesomaior = temp[1]

    pessoas.append(temp[:])
    temp.clear()

    resp = ''
    while True:
        resp = input('Quer continuar? [S/N] \n >>').upper().strip()[0]

        if resp in 'SN':
            break

    if resp == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {pesomaior:.0f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesomaior:
        print(f'[{p[0]}]', end=' ')

print()
print(f'O menor peso foi de {pesomenor:.0f}Kg. Peso de ', end='')

for p in pessoas:
    if p[1] == pesomenor:
        print(f'[{p[0]}]', end=' ')
