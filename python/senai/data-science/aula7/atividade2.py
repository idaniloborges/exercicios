# ATIVIDADE 2:

# Crie um array 2D de tamanho (5, 5) com valores aleatórios entre 0 e 100.

# Calcule a média de cada linha.

# Encontre o valor máximo e mínimo de toda a matriz.

import numpy as np

rng = np.random.default_rng()
matriz = rng.integers(100, size=(5, 5))
maior_valor = []
menor_valor = []

print(matriz)

for conjunto in matriz:
    print(f'{np.mean(conjunto)}')
    maior_valor.append(max(conjunto))
    menor_valor.append(min(conjunto))

print(f'Menor valor: {min(menor_valor)}')
print(f'Maior valor: {max(maior_valor)}')

