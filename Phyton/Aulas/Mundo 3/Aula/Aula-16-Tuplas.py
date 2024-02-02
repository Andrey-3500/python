#Variaveis Compostas

# TUPLAS - uma tupla é definida com () paranteses
# * Tuplas são imutaveis durando a execução do programa

tupla = ('batata', 'macarrão', 'arroz', 'feijão')

for comida in tupla:
    print(comida)

for cont in range(0, len(tupla)):
    print(f'Eu vou comer {tupla[cont]}')

for pos, comida in enumerate(tupla):
    print(f'eu vou comer {comida} na posição {pos}')

# somando tuplas

a= (1,2,3,4)
b= (9,8,7,6,5)

# quando somamos tuplas, a ordem tem total infuência
# somar a + b é diferente do que somar b + a

c = a + b
print(c)
c = b + a
print(c)
# usando Sorted é colocado em ordem más não altera a tupla

# temos a propriedade INDEX em Tuplas

b= (9,8,7,6,5)
print(sorted(b))
# se colocarmos b.index(7) ele nos dá a posição do numero 7, ou seja ele nos responde 2

print(b.index(7))

# se colocarmos virgula após o numero escolido ex b.index(7, ) podemos escolher apartir de qual posição
#exemplo

print(b.index(7, 3))
# eu evou pedir o numero 7 a partir da posição 3

# tuplas aceita qualquer tipo de dados

pessoa = ('Andrey', 20, 'M', 106)

# as tuplas só podem ser deletadas por inteiro, não somente um dado









