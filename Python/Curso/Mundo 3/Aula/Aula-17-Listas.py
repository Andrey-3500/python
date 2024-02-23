#Variaveis Compostas


# LISTAS - uma Lista é definida com [] colchetes
# * Lista são mutaveis durando a execução do programa

num = [2, 5, 9, 1]

num[2] = 3  #Diferente de Tuplas, em Listas podemos alterar os valores.

num.append(7) #Podemos adicionar valores

num.sort(reverse=True) #O .sort mostra os numeros em sequencia com reverse nos dá a ordem de de trás pra frente
print(num)

print(len(num)) #O len serve pra no mostrar a quantidade de elementos

num.insert(2, 0) #com insert eu escolho a (posição e o valor) que quero adicionar

print(num)

num.pop() #usando .pop removemos elementos, caso não tenha um indice, será removido o ultimo

print(num)

num.remove(2)#no .remove remove por valor e não por posição (removendo o primeiro valor que for encontrado)
# no caso de .remove caso o valor não seja encontrado, o programa dá erro!
# por isso devemos usar estruturas de condição.

print(num)

#neste exemplo não é encontrado o numero na lista

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número')

print(f'lista depois da condição : {num}')

#neste exemplo é encontrado o numero na lista

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número')

print(f'lista depois da condição : {num} assim removendo o numero 5')

