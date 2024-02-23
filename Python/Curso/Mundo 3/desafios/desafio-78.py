valores = []
pmaior = pmenor = 0

for c in range(0, 5):

    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

    if c == 0:
        maior = menor = valores[c]

    else:
        if valores[c] > maior:
            maior = valores[c]

        elif valores[c] < menor:
            menor = valores[c]

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado e foi o {maior} nas posições ', end='')

for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}.. ', end='')

print(f'\nO menor valor digitado e foi o {menor} nas posições ', end='')

for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}.. ', end='')
