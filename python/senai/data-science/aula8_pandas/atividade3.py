# 3 - EXPLOQUE A DOCUMENTAÇÃO 
# https://numpy.org/doc/stable/

# Filtre apenas as vendas maiores que 100.

# Calcule quantas vendas ficaram abaixo da média.

# Crie um novo array com os valores (divida cada valor pelo máximo).

import numpy as np


maiores_que_100 = []
menores_que_media = []
divisao = []

vendas = np.array([120,90,150,80,200,110,50,300])
media = np.mean(vendas)
valor_maximo = max(vendas)

print(f'Media: {media}')


for valor in vendas:
    divisao.append(valor / valor_maximo)
    if valor > 100:
        maiores_que_100.append(valor)
    if valor < media:
        menores_que_media.append(valor)
        # print(valor)

print(f'Valores maiores que 100: {maiores_que_100}')
print(f'Quantidade de vendas abaixo da média: {len(menores_que_media)}')
print(f'Valores dividos pelo maior valor: {divisao}')