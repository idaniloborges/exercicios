import pandas as pd

dados = pd.read_csv('dados.csv')

print(dados)


# Ler arquivos
# df = pd.read_

# Ler as primeiras linhas de um data_frame
# df.head()

# Ler as últimas linhas de um data_frame
# df.tail()

# Verificar a forma de uma data_frame
# df.shape

# Obter um resumo estatístico das colunas numéricas:
# df.describe()

# Verificar os tipos de dados das colunas:
# df.dtypes

# Adicionar uma nova coluna:
# df['nova_coluna'] = valor

# Excluir uma coluna:
# df.drop('coluna', axis=1, inplace=True)

# Salvar DataFrame em um arquivo JSON:
# Salvar DataFrame em um arquivo JSON:

import pandas as pd 


dados  =  pd.read_csv('teste/code.csv')
# print(dados['vendedor'])


df  =  pd.DataFrame(dados)


# 5 primeiras linhas 
# print(df.head())


# 5 ultimas
# print(df.tail())


# estatica basica 
# print(df.describe())


# dados tecnicos da estrutura de dados
# print(df.info())


# acessando indices das colunas 
# print(df['vendas'][10])


# print(df[df['vendas'] >= 25000])


# linha especifico 
# print(df.iloc[5])


# pd.set_option('display.max_rows', None)


# print(df.to_string())


# atribuição de nova linha e nova coluna


# df['nova coluna'] =  df['vendas'] +  20


# df.rename(columns = {
# 'vendas':'novas_vendas',
# 'vendedor':'nome_vendedores',
# 'mês': 'novo_Mês'


#      },inplace=True)


# print(df)


# pd.reset_option('display.max_columns')
# pd.reset_option('display.max_rows')



# mostra onde pe a linha
# print(df.isnull())



# remover a linha que possui dados faltantes 
# df.dropna(inplace=True)


# print()


# df.fillna(0, inplace=True)



# media_vendedor = df.groupby('vendedor')['vendas'].mean()
# print(media_vendedor)


# print(df)