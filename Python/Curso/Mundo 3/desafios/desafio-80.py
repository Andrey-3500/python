valores = []

for c in range(0, 5):
    valor = int(input(f'Digite um valor: '))
    if c == 0:
        valores.append(valor)
        print(f'Primeiro número Adicinado...')
    q = len(valores) - 1

    for p, v in enumerate(valores):

        if valor not in valores:
            if valor < valores[p]:
                valores.insert(p, valor)
                print(f'Adicinado na posição {p}')
            if valor > valores[q]:
                valores.append(valor)
                print('Adicionado ao final da lista...')

print(f'Os valores adicionados foram {valores}')