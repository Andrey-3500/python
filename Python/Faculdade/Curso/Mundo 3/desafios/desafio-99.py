from time import sleep
from random import randint
def maior(* valor):

    print('Analisando os valores passados...')
    maior = 0
    for p in (valor):

        print(p, end=' ')
        sleep(0.5)

        if p > maior:
            maior = p

    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-'*50)


maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
