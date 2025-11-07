



#8 -  agregação com o groupby()

import pandas as pd

#1 -  Lendo o arquivo CSV
dados = pd.read_csv('dados_exercicio1.csv')
# print(dados)

#2 -  crie um dataFrame
df = pd.DataFrame(dados)
print(df)

#3 -  calcule a média de idade
media_idade = df['Idade'].mean()
print(f''' --------  Média das idades -------- 
      {media_idade}''')

#4 -  mediana de idade
mediana_idade = df['Idade'].median()
print(f''' --------  Mediana das idades -------- 
       {mediana_idade}''')

#5 -  busque os dados da Maria 
dados_maria = df[df['Nome'] == 'Maria']
print(f''' -------- Dados Maria --------  
      {dados_maria}''')

#6 -  verifique as informações do csv
# informacoes = df.info()
print(f'''-------- Informações da tabela -------- ''')
print(df.info())

#7 -  traga descrição básica
descricao = df.describe()
print(f'''-------- Descrição da tabela -------- 
      {descricao}''')