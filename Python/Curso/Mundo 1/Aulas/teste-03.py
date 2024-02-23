
media = 0
nomes = []
idades = []
sexos = []
resultados = []
tupla = []

for c in range (0, 2):
    nome = (input('Digite seu nome \n >> '))
    idade = int(input('Digite sua idade \n >> '))
    #sexo = (input('Digite seu sexo \n >> '))

    nomes.append(nome)
    idades.append(idade)
    #sexos.append(sexo)

    for i in range(2):
        tupla = (nomes[i], idades[i])
        resultados.append(tupla)
    print(resultados)

