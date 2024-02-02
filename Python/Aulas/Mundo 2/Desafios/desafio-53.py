frase = str(input('Digite sua frase \n >> ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo!')
