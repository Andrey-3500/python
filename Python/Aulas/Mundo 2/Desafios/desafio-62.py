print('=='*14)
print('    GERADOR DE PA')
print('=='*14)

termo = int(input('Primeiro termo: '))
razão = int(input(('Razão: ')))

décimo = termo + (10 - 1) * razão

p = termo
cont = 0
c = 0
while p != décimo + razão:

    print('{} ->'.format(p), end=' ')
    p += razão
    cont += 1
    if cont == 10:
        c = int(input('\n Gostaria de ver mais quantos termos? \n >> '))
        cont -= c
        if c != 0:
            décimo = décimo + razão * c

print('Acabou')