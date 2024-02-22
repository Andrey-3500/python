ano = int(input('Que ano quer analisar '))

bi = ano % 4

if bi == 0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))
