print('-'*40)
print('Analizador de Triângulos')
print('-'*40)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 + r2 >= r3 and r2 + r3 >= r1 and r1 + r3 >= r2:
    print('Os segmentos acima PODEM FORMAR triângulo,')
    if r1 == r2 == r3:
        print('eles formam um triângulo EQUILÁTERO')
    if r1 != r3 and r3 != r2 and r2 != r1:
        print('eles formam um triângulo ESCALENO')
    if r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('eles formam um triângulo ISÓSCELES')
    if (r1**2) + (r2**2) == r3**2 or (r3**2) + (r2**2) == r1**2 or (r3**2) + (r1**2) == r2**2:
        print('eles formam um triângulo RETANGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
