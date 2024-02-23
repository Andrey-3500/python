from uteis.numeros import moeda

p = float(input('Digite um valor R$ '))

print(f'A metade de {moeda.m(p)} é {moeda.m(moeda.metade(p))}')
print(f'O dobro de {moeda.m(p)} é R${moeda.m(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.m(p)} é {moeda.m(moeda.aumentar(p))}')
print(f'Reduzindo 13% de {moeda.m(p)} é {moeda.m(moeda.reduzir(p))}')