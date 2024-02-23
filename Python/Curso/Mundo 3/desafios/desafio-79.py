valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        print('Valor adicionado com sucesso...')
        valores.append(valor)
    else:
        print('\033[31mErro!\033[m valor já listado, Não adicionado.')

    r = ''
    while True:
        r = str(input('Quer continuar? [S/N]\n>> ')).strip().upper()[0]

        if r in 'NnSs':
            break

    if r == 'N':
        break

valores.sort()
print(f'Os valores adicionados foram {valores}')