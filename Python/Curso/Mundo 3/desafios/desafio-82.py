valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))

    r = ''
    while True:
        r = str(input('Quer continuar ? [S/N] \n>>')).upper().strip()[0]

        if r in 'SN':
            break
    if r == 'N':
        break

for c in range(0, len(valores)):

    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])

print(f'A lista completa é {valores}')
print(f'A lista dos valores pares é {pares}')
print(f'A lista dos valores impares é {impares}')