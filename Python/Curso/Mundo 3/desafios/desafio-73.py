times = ('Atlético-PR', 'Flamengo', 'Chapecoense', 'Palmeiras', 'Fluminense', 'América-MG',
         'São Paulo', 'Grêmio', 'Vasco', 'Botafogo', 'Sport', 'Cruzeiro', 'Vitória', 'Santos',
        'Atlético-MG', 'Internacional','Corinthians', 'Bahia', 'Ceará', 'Paraná')


print('-'*40)
print('Os 5 primeiros colocados são:')
for pri in range (0,5):
    print(f' {pri+1}º {times[pri]}')

# print (f'{times[0:5]') também mostra os 5 primeiros

print('-'*40)
print('Os 4 ultimos colocados são:')

for pri in range (-4,0):
    print(f' {pri+21}º {times[pri]}')

# print (f'{times[-4:]') também mostra os 4 ultimos

print('-'*40)
print('Os times em ordem alfabetica é:')
print(sorted(times))

print('-'*40)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
