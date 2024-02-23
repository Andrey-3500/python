from time import sleep
from emoji import emojize
print('Contagem regressiva para os fogos')
for c in range(10, 0, -1):
    print(c)
    sleep(0.5)
print(emojize(':collision:'))