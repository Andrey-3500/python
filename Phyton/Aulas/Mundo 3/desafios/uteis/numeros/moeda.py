def metade(v=0, show=False):
    v /= 2
    return v if show is False else m(v)
        

def dobro(v=0, show=False):
    v *= 2
    return v if show is False else m(v)
   

def aumentar(v=0, show=False):
    v += (v * 10/100)
    return v if show is False else m(v)
   

def reduzir(v=0, show=False):
    v -= (v * 13/100)
    return v if show is False else m(v)
   

def m(v=0):
    return (f'R${v:.2f}')


def resumo(v, a, r):

    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado:    R${v:.2f}')
    print(f'Metade do preço:    R${v / 2:.2f}')
    print(f'Dobro do preço:     R${v * 2:.2f}')
    print(f'{a}% de aumento:     R${v + (v * a/100):.2f}')
    print(f'{r}% de redução:     R${v - (v * r/100):.2f}')
    print('-'*30)
