
def fatorial(num, show=False):
    '''
    --> Calcula o Fatorial de um número.
    :param num: O númro a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    '''
    for v in range(num-1, 0, -1):
        num *= v
        if show:
            print(v, end='')
            if v > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return num


print(fatorial(5))
