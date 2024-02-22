def fatorial(n):
    f= 1
    for c in range(1, n+1):
        f *= c
    return f

def leiaInt(msg):

    while True:

        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue

        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0

        else:
            return n

def leiaFloat(msg):

    while True:
        try:
            n = float(input(msg).replace(',','.').strip())

        except (ValueError, TypeError):
            print('ERRO: por faver, digite um número real válido.')
            continue

        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0

        else:
            return n

