
print(f'{" Calculadora de anos ":-^50}')
print('Digite a 1º data')

dia1 = int(input('dia: '))
mes1 = int(input('mês [01|12]: '))
ano1 = int(input('ano: '))

print('-'*30)

print('Digite a 2º data')
dia2 = int(input('dia: '))
mes2 = int(input('mês [01|12]: '))
ano2 = int(input('ano: '))

print('-'*30)

diasano1 = dia1 + (mes1 * 30.41) + (ano1 * 365.25)

diasano2 = dia2 + (mes2 * 30.41) + (ano2 * 365.25)

ano3 = diasano2 - diasano1

if ano3 < 0:
    ano3 *= -1

print(F'A diferença entre as datas digitadas foi {ano3:.0f} Dias')
