def terreno(area):
    print(f'A área de um terreno de {lar}x{com} é de {area}m².')

print()
print('Controle de Terrenos')
print('-'*25)

lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))

terreno(lar*com)