print('=='*14)
print('    GERADOR DE PA')
print('=='*14)

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

pri = termo
cont = 0
total = 0
mais = 10
while mais !=0:
    total = mais + total
    while cont <= total:

        print('{} ->'.format(termo), end=' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('\n Gostaria de ver mais quantos termos? \n >> '))
print('Fim')
