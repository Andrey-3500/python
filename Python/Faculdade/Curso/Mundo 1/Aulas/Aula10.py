#simples

nome = str(input('Qual é o seu nome? '))
if nome == 'Andrey':
    print('Que nome lindo vc tem!')
print('Bom dia, {}'.format(nome))

#Composta

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

m = (n1+n2)/2

print('A sua média foi {:.1f}'.format(m))

if m >= 6:
    print('Parabéns')
else:
    print('Estude mais!')

#simplificado

#n1 = float(input('Digite a primeira nota:'))
#n2 = float(input('Digite a segunda nota:'))

#m = (n1 + n2) / 2

#print('Parabéns' if m >= 6 else 'Estude mais!')
