from time import sleep
def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio > fim and passo > 0:
        passo *= -1

    for p in range(inicio, fim+passo, passo):

        print(p, end=' ')

        sleep(0.5)

    print('Fim!')
    print('-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem !')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
