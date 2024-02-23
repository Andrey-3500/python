from random import randint

print('-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-'*30)

vencidas = 0
resultado = ' '
while True:

    valor = int(input('Diga um valor \n >> '))
    computador = randint(0, 10)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] \n >> ')).upper().strip()[0]
        print('-' * 50)

    soma = valor + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    print(f'Você jogou {valor} e o comutador {computador}. Total de {soma} DEU {resultado}')
    print('-' * 50)

    if escolha == resultado[0]:
        print('Você VENCEU!\nVamos jogar novamente..')
        print('-' * 50)
        vencidas += 1
    else:
        print('Você PERDEU!')
        print('-' * 50)
        break

print(f'GAME OVER! Você venceu {vencidas} vezes')