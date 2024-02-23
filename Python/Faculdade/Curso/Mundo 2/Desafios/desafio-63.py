seq = int(input('Digite quantos numeros da sequencia gostaria de ver \n >> '))
var1 = fib = 1
var2 = 0
cont = 0

while cont != seq:

    if cont != seq:
        print(var2 ,'->', end=' ')
        cont += 1
    else:
        break

    if cont != seq:
        print(fib,'->', end=' ')
        cont += 1
    else:
        break

    if cont != seq:
        print(var1,'->', end=' ')
        cont += 1
    else:
        break

    var2 = var1 + fib

    fib = var1 + var2

    var1 = fib + var2
print('Fim')