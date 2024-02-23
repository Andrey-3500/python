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

def linha(t = 40):
    return '-' * t

def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):

    cabeçalho('MENU PRINCIPAL')
    c = 1
    
    for item in lista:
        print (f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc