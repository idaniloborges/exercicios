# 3 -  MANIPULE AS TEMPERATURAS


# Filtre apenas as temperaturas acima de 24 graus.

# Calcule quantas temperaturas ficaram acima da média.

# Crie um novo array com os valores normalizados 
# (subtraia a média e divida pelo desvio padrão).


import numpy as np


temperaturas = np.array([22, 25, 19, 30, 28, 21, 18, 33])

maiores_que_24 =[]
maiores_que_media = []
media = np.mean(temperaturas)
desvio_padrao = np.std(temperaturas)
novo_array = []

for temperatura in temperaturas:
    novo_array.append((temperatura-media)/desvio_padrao)
    
    if temperatura > 24:
        maiores_que_24.append(temperatura)
    if temperatura > media:
        maiores_que_media.append(temperatura)



