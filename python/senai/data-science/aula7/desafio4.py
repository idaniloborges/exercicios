# DESAFIO  4 :

# A empresa de **cartões de crédito enfrenta uma crescente perda de clientes** e 
# **deseja compreender os fatores que levam ao cancelamento dos cartões**. 
# Para isso, realize uma análise de dados a partir de uma planilha contendo informações dos clientes, 
# com o objetivo de identificar padrões e traçar o possível motivo da perda dos clientes.

# 1 - identificar o problema
# 2 - Objetivo
# Utilize media moda mediana desvio padrão.

import statistics

clientes = [
{"Idade": 45, "Limite": 12691, "Meses_cliente": 39, "Taxa_utilizacao": 0.061},
{"Idade": 49, "Limite": 8256, "Meses_cliente": 44, "Taxa_utilizacao": 0.105},
{"Idade": 51, "Limite": 3418, "Meses_cliente": 36, "Taxa_utilizacao": 0},
{"Idade": 40, "Limite": 3313, "Meses_cliente": 34, "Taxa_utilizacao": 0.76},
{"Idade": 40, "Limite": 4716, "Meses_cliente": 21, "Taxa_utilizacao": 0},
{"Idade": 44, "Limite": 4010, "Meses_cliente": 36, "Taxa_utilizacao": 0.311},
{"Idade": 51, "Limite": 34516, "Meses_cliente": 46, "Taxa_utilizacao": 0.066},
{"Idade": 32, "Limite": 29081, "Meses_cliente": 27, "Taxa_utilizacao": 0.048},
{"Idade": 37, "Limite": 22352, "Meses_cliente": 36, "Taxa_utilizacao": 0.113},
{"Idade": 48, "Limite": 11656, "Meses_cliente": 36, "Taxa_utilizacao": 0.144},
{"Idade": 42, "Limite": 6748, "Meses_cliente": 31, "Taxa_utilizacao": 0.217},
{"Idade": 65, "Limite": 9095, "Meses_cliente": 54, "Taxa_utilizacao": 0.174},
]

idades = [c['Idade'] for c in clientes]
limite = [c['Limite'] for c in clientes]
taxas = [c['Taxa_utilizacao'] for c in clientes]
taxa_zero = [c['Taxa_utilizacao'] for c in clientes if c['Taxa_utilizacao'] == 0]
alto_uso = [c for c in clientes if c['Taxa_utilizacao'] > 0.5]

print(f'Média idade: {statistics.mean(idades):.2f}')
print(f'Média de taxa de utilização: {statistics.mean(taxas):.2f}')
print(f'Menor limite: {min(limite)}')
print(f'Média limites: {statistics.mean(limite):.2f}')
print(f'Mediana limites: {statistics.median(limite):.2f}')
print(f'Maior limite: {max(limite)}')

print(taxa_zero)
print(alto_uso)
