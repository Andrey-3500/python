while True:
    valor = int(input('Quer ver a tabuada de qual valor? \n >> '))
    print('-'*20)
    if valor < 0:
        break
    for c in range (1, 11):
        print(f'{valor} x {c} = {c*valor}')
    print('-' * 20)
print('Programa tabuada encerrado. Volte sempre!')
