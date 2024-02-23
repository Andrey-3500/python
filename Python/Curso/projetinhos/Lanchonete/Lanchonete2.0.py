produtos = [(100,'Cachorro-Quente',9), (101,'Cachorro-Quente Duplo', 11),(102,'X-Egg', 12),(103,'X-Salada',13),(104,'X-Bacon',14),(105,'X-Tudo', 17),(200,'Refrigerante Lata',5),(201,'Chá Gelado',4)]

print('{:-^51}'.format(' CARDAPIO '))
print('\033[34m{0:<}\033[m|\033[33m{1:^30}\033[m|\033[32m{2:>}\033[m'.format('Código', 'Descrição','Valor(R$)'))
print('-'*50)

for c in range(0, 8):
    print('\033[34m{0:<6}\033[m|'.format(produtos[c][0]), end='')
    print('\033[33m{0:^30}\033[m|'.format(produtos[c][1]), end='')
    print(' \033[32mR${0:>6.2f}\033[m'.format(produtos[c][2]))
print('-'*50)

pedido = []
opção = total = quantidade = 0
while True:

    while True:
        opção = int(input('Qual é o seu pedido ?\n >> '))
        print('\033[30m-\033[m'*50)
        tentativa = False

        for x in range(0, 8):
            if opção == produtos[x][0]:
                pedido.append(produtos[x])
                tentativa = True


        if tentativa == False:
            print('\033[31m Opção Invalida! \033[m')
        else:
            break

    opção2 = ' '
    while opção2 not in 'SN':
        opção2 = str(input('Quer pedir algo mais ? \n [S/N] >> ')).upper().strip()[0]
        print('\033[30m-\033[m' * 50)
    if opção2 == 'N':
        break

quantidade = (len(pedido))
print('Seu pedido foi :')
for y in range(0, quantidade):

    print(f'{y + 1}ª{pedido[y][1]:^25}R${pedido[y][2]:.2f}')
    total += pedido[y][2]

print('\033[30m-\033[m' * 50)
print(f'O total do seu pedido foi de R${total:.2f}\n')