print('-'*25)
print('|| CALCULADORA ||')
print('-'*25)

print('[1]Soma')
print('[2]Subtração')
print('[3]Divisão')
print('[4]Multiplicação')
print('[5]Porcentagem')


print('-'*40)
esc = int(input('Qual dessas opções gostaria de fazer: '))
print('-'*40)


if esc == 1:
    print('SOMA')
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    print('{} + {} = {}'.format(n1, n2, (n1 + n2)))

elif esc == 2:
    print('  '*3, 'SUBTRAÇÃO')
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    print('{} - {} = {}'.format(n1, n2, (n1 - n2)))

elif esc == 3:
    print('  '*3, 'DIVISÃO')
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    print('{} / {} = {:.2f}'.format(n1, n2, (n1 / n2)))

elif esc == 4:
    print('  '*3, 'MULTIPLICAÇÃO')
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    print('{} * {} = {}'.format(n1, n2, (n1 * n2)))

elif esc == 5:
    print('  '*3, 'PORCENTAGEM')
    n1 = float(input('digite o numero: '))
    n2 = float(input('digite a porcentagem: '))
    print('{} % {} = {:.1f}'.format(n1, n2, (n1 * n2/100 )))
else:
    print('Você escolhe nenhuma das opções')