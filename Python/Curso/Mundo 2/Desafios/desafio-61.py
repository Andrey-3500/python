print('=='*14)
print('    10 TERMOS DE UMA PA')
print('=='*14)

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

décimo = termo + (10 - 1) * razão

p = termo
cont = 0

while p != décimo + razão:
    print('{} ->'.format(p), end=' ')
    p += razão
    cont += 1

print('Fim do programa!')