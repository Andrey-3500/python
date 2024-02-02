palavras = ('AZEDO', 'OLEO', 'APRENDER', 'FEITO', 'SUSPEITO','SUSPIRO', 'SANTO', 'ANDREY CORREIA DOS SANTOS')

for c in palavras:
    print(f'\nna palavra {c} temos: ',end='')

    for letra in c:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
