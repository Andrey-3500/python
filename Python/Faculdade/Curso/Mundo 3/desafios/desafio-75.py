valores = (int(input('Digite um numero: ')),
            int(input('Digite outro numero: ')),
            int(input('Digite mais um numero: ')),
            int(input('Digite um ultimo numero: ')))

contnove = conttres = 0
pares = []
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu {valores.index(3)+1}º posição')
else:
    print('O valor 3 não foi declarado')
print('Os valores pares digitados foram ',end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
