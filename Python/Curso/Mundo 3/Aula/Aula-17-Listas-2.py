valores = []
valores.append(5)
valores.append(3)
valores.append(6)

for v in valores: #para cada valor em valores:
# (em vez de range é para cada valor dentro da lista)
    print(f'{v}..', end=' ')


for c, v in enumerate(valores): #para cada valor em valores,
# enumerando de acordo com a sua chave :

    print(f'\n na posição {c} é o valor {v}')

print('Fim da lista')

lista1 = []


for cont in range (0,5): # assim os valores digitados é adicionado em uma lista
    lista1.append(int(input('Digite um valor: ')))
print(lista1)


# PECULIARIDADE DE LISTA EM PYTHON

a = [1,4,5]

b = a # assim as lista recebem uma ligação, sempre igualando
# para fazer uma copia e não uma ligação é com, b = a[:]
# B (recebendo), (todos os valore [:]), de A
# assim criando uma cópia e não uma ligação

print(a)
print(b)

# assim alterando uma delas, a alteração é feito nas duas listas

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
