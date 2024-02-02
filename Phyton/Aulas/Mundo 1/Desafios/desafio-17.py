from math import hypot
opos = float(input('Comprimento do cateto oposto: '))
adja = float(input('Comprimento do cateto adjacente: '))
hi = hypot(opos, adja)
print("A hipotenusa vai medir {:.2f}".format(hi))