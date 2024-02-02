n = int(input('Digite um número para ver sua tabuada: '))

print('_'*15)
for c in range (1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
    c += 1
print('_'*15)