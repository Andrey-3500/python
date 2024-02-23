def escreva(txt):
    print('~' * (len(txt)+2))
    print(f'{txt}')
    print('~' * (len(txt)+2))


escreva(f'{"Olá mundo !":^15}')
escreva(f'{"Andrey Correia dos Santos":^33}')
