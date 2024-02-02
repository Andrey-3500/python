from random import randint
print('---'*20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('---'*20)
nj = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
nc = randint(0, 5)
print('PARABÉNS! Você conseguiu me vencer!' if nj == nc else 'GANHEI Eu pensei no número {} e não no {}'.format(nc, nj))

#composto
#if n == nc:
#    print('PARABÉNS! Você conseguiu me vencer!')
#else:
#   print('GANHEI Eu pensei no número {} e não no {}'.format(nc, n))
