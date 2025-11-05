# DADO UMA FEQUÊNCIA , UTILIZE A CALCULADORA E O UM ARQUIVO TXT, PARA FAZER OS CALCULOS:

import functions

lista_frequencias = [[1,2,3,6,4], [1.5,6.8,9.7,10.6], [200,300,500,700,900,400,600]]

for amostra in lista_frequencias:
    print(f'-------- AMOSTRA {lista_frequencias.index(amostra)+1} --------')
    functions.media(amostra)
    functions.moda(amostra)
    functions.mediana(amostra)
