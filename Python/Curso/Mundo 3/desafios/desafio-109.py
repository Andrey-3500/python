from uteis.numeros import moeda

p = float(input('Digite um valor R$ '))

print(f'A metade de {moeda.m(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.m(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, True)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(p, True)}') 
