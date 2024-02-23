print('=='*14)
print('    10 TERMOS DE UMA PA')
print('=='*14)

termo = int(input('Primeiro termo: '))
razão = int(input(('Razão: ')))
Pa = termo

décimo = termo + (10 - 1) * razão

for c in range (termo, décimo + razão, razão):

   print('{}'.format(c), end=' ')

print('Acabou')