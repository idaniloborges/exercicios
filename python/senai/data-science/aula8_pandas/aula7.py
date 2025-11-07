# import timeit
import numpy as np
import pandas as pd

# Teste de velocidade
# def soma1 ():
#     lista  =  [1,2,3]
#     print(lista)
#     return lista


# soma1()
# time = timeit.timeit(soma1, number=10)
# print('função1', time)


# def soma2():
#       lista = np.array([1,2,3])
#       print(lista)
#       return lista 


# time = timeit.timeit(soma2, number=10)
# print('função2', time)


dados = pd.read_csv('dados_vendas.csv')
# print(dados)

df = pd.DataFrame(dados)
print(f'''Primeiras 10 linhas da tabela:
       {df.head(10)}''')

media_vendas_ano = df.groupby('ano')['vendas'].mean()
print(f'''----- Média de vendas por ano -----:
       {media_vendas_ano}''')



media_vendas_produto = df.groupby('produto')['vendas'].mean()
print(f'''----- Média de vendas por produto -----:
       {media_vendas_produto}''')

media_lucro_produto = df.groupby('produto')['lucro'].mean()
print(f'''----- Média de lucro por produto -----: 
      {media_lucro_produto}''')
