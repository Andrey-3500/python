print('-'*25)
print('{0:^25}'.format('CALCULADORA'))
print('-'*25)

print('[1]Soma \n[2]Subtração \n[3]Divisão \n[4]Multiplicação \n[5]Porcentagem \n[6]Terminar ')
esc = 0
while True:
    print('-' * 25)
    esc = int(input('opção >> '))
    print('-' * 25)

    if esc == 1:
        print('{0:^25}'.format('SOMA'))
        n1 = float(input('digite o primeiro numero: '))
        n2 = float(input('digite o segundo numero: '))
        print(f'{n1} + {n2} = {n1 + n2}')

    elif esc == 2:
        print('{0:^25}'.format('SUBTRAÇÃO'))
        n1 = float(input('digite o primeiro numero: '))
        n2 = float(input('digite o segundo numero: '))
        print(f'{n1} - {n2} = {n1 - n2}')

    elif esc == 3:
        print('{0:^25}'.format('DIVISÃO'))
        n1 = float(input('digite o primeiro numero: '))
        n2 = float(input('digite o segundo numero: '))
        print(f'{n1} / {n2} = {n1 / n2}')

    elif esc == 4:
        print('{0:^25}'.format('MULTIPLICAÇÃO'))
        n1 = float(input('digite o primeiro numero: '))
        n2 = float(input('digite o segundo numero: '))
        print(f'{n1} x {n2} = {n1 * n2}')

    elif esc == 5:
        print('{0:^25}'.format('PORCENTAGEM'))
        n1 = float(input('digite o numero: '))
        n2 = float(input('digite a porcentagem: '))
        print(f'{n1} % {n2} = {n1 * (n2/100)}')
    elif esc == 6:
        break
    else:
        print('Opção invalida!\nTente novamente!')
print("Fim do programa")