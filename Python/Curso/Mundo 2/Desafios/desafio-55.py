maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso em da {}ª pessoa \n >> '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso

print('O maior peso digitado foi {}Kg \n e o menor foi {}Kg'.format(maior, menor))

