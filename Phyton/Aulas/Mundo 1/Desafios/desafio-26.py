frase = str(input('Digite uma frase:')).strip().lower()
print('A letra A aparece {} vezes na frase.' .format(frase.count('a')))
print ('a primeira letra A, apareceu na posição {}'.format(frase.find('a')+1))
print('a ultima letra A, apareceu na posição {}'.format(frase.rfind('a')+1))