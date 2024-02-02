# LISTA DENTRO DE LISTA

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

pessoas = [['joão', 19],['maria', 29],['Joaquim',11]]

for p in pessoas:
    print(f'a pessoa {p[0]} tem {p[1]}')