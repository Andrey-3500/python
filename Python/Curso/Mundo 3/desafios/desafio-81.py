valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = ''
    while True:
        r = str(input('Quer continuar ? [S/N] \n >>')).upper().strip()[0]

        if r in 'SsNn':
            break

    if r in 'Nn':
        break

print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'O valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
