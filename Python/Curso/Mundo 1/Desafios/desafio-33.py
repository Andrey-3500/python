v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

if v1<v2 and v1<v3:
    menor = v1

if v2<v1 and v2<v3:
    menor = v2

if v3<v1 and v3<v2:
    menor = v3

if v3==v1 and v3==v2:
    menor = v1
    print('Todos os valores são iguais')

print('O menor valor digitado foi {}'.format(menor))

if v1>v2 and v1>v3:
    maior = v1

if v2>v1 and v2>v3:
    maior = v2

if v3>v1 and v3>v2:
    maior = v3

if v3==v1 and v3==v2:
    maior = v3
    print('nenhum valor é maior')

print('O maior valor digitado foi {}'.format(maior))
