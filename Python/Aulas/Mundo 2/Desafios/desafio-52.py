numero = int(input('Digite um numero: '))
qnt = 0
for c in range(1, numero + 1):

    if numero % c == 0:
        print('\033[34m', end='')
        qnt += 1
    else:
        print('\033[31m',end='')
    print('{}'.format(c), end=' ')

print('\n\033[mo número {} foi divisível {} vezes'.format(numero, qnt))


if qnt == 2:
    print('E por isso {} \033[34m é PRIMO'.format(numero))
else:
    print('E por isso {} \033[31m NÃO È PRIMO'.format(numero))

