from uteis.numeros import moeda
from uteis.utilidades import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 10)