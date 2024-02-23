print('-'*30)
print('{:^30}'.format('Lojão do CEV'))
print('-'*30)

total = maismil = menor = 0
nomemenor = ''

while True:

    nome = str(input('Produto: '))
    preço = float(input('Preço do produto R$'))
    total += preço

    if menor == 0 or menor > preço:
        menor = preço
        nomemenor = nome

    if preço > 1000:
        maismil += 1
    resposta = ' '

    while resposta not in 'SN':
        resposta = str(input('Comprou algo mais ? [S/N] \n >>')).upper().strip()[0]

    if resposta == 'N':
        break

print('-'*12, 'FIM DO PROGRAMA', '-'*12)
print(f'No total você gastou R${total:.2f}\n'
      f'{maismil}produtos custam mais de R$1000.00\n'
      f'O/A {nomemenor} foi o produto mais barato')



