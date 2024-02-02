#Variaveis Compostas

# DICIONÁRIOS - um Dicionário é definido com {} chaves
# * com dicionários podemos mudar o indice  por exemplo:

dados = {}
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
# Assim ao inves de dados[0] usamos ['nome'] <-- Chamamos de Elemento
# Para adicionar Elementos não usamos o append usamos:

dados['sexo'] = 'M'
# Para remover Elementos usamos del.

# Itens = .items() <--  são os ambos elementos e valores
# Chaves = .keys() <-- os Elementos
# Valores = .values() <-- todos os valores

pessoa = {'nome': 'Andrey', 'Sexo':'M', 'idade': 20}
# adicionando itens
pessoa['peso'] = 106

print('.keys () <- Chaves')
for k in pessoa.keys():
    print(k)
print()

print('.values () <- valores de cada chave')
for k in pessoa.values():
    print(k)
print()

print('.items() <- chaves e valores')
for k, v in pessoa.items():
    print(f'{k} = {v}')

# para colocar um dicionario dentro de uma lista,
# ao inves de usarmos .append(discionario[:])
# usamos .append(discionario.copy())