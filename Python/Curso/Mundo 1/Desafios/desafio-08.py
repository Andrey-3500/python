d = float(input('Digite ma distância em metro: '))
print('A medida de {}m corresponde a \n{}km \n{:.3f}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm '.format(d, d/1000 ,d/100, d/10, d*10, d*100, d*1000))
