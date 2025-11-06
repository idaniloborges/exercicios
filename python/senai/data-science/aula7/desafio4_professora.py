import statistics



clientes = [
{"Idade": 45, "Limite": 12691, "Meses_cliente": 39, "Taxa_utilizacao":0.061},
{"Idade": 49, "Limite": 8256, "Meses_cliente": 44, "Taxa_utilizacao":0.105},
{"Idade": 51, "Limite": 3418, "Meses_cliente": 36, "Taxa_utilizacao":0},
{"Idade": 40, "Limite": 3313, "Meses_cliente": 34, "Taxa_utilizacao":0.76},
{"Idade": 40, "Limite": 4716, "Meses_cliente": 21, "Taxa_utilizacao":0},
{"Idade": 44, "Limite": 4010, "Meses_cliente": 36, "Taxa_utilizacao":0.311},
{"Idade": 51, "Limite": 34516, "Meses_cliente": 46, "Taxa_utilizacao":0.066},
{"Idade": 32, "Limite": 29081, "Meses_cliente": 27, "Taxa_utilizacao":0.048},
{"Idade": 37, "Limite": 22352, "Meses_cliente": 36, "Taxa_utilizacao":0.113},
{"Idade": 48, "Limite": 11656, "Meses_cliente": 36, "Taxa_utilizacao":0.144},
{"Idade": 42, "Limite": 6748, "Meses_cliente": 31, "Taxa_utilizacao":0.217},
{"Idade": 65, "Limite": 9095, "Meses_cliente": 54, "Taxa_utilizacao":0.174},
]



idades =  [c['Idade'] for c in clientes]
limites = [c['Limite'] for c in clientes]
taxas =   [c['Taxa_utilizacao'] for c in clientes]
meses =   [c['Meses_cliente'] for c in clientes]


print('Média idade:',round(statistics.mean(idades)))
print('Média Limites:',round(statistics.mean(limites)))
print('Mediana Limites', statistics.median(limites))
print('DESvio Liimites', statistics.stdev(limites))
print('Moda Limites', statistics.mode(limites))
print('Média Taxa:',round(statistics.mean(taxas)))
print('Media Meses ', statistics.mean(meses))




print('Clientes com taxa zero de utilização')
taxa_zero = [c for c in clientes if c['Taxa_utilizacao'] == 0]
print(taxa_zero)
print('taxa zero', len(taxa_zero))
alta_uso = [c for c in clientes if c['Taxa_utilizacao'] > 0.5]
print('alta em uso',len(alta_uso))



# insight 
# media das pessoas que utilizam os cartões adultas
# 25% clientes nao usaram o cartão 
# alto limites 
# clientes mais velhos possuem relação mais longa  


# tomada de decisão 


# contatar clientes inativos acentuar os benedficios que o cartão oferece
# criar convenios com famarcias gerando beneficios para os usuarios
# Criar novos incentivos de fidelização
# reajustar limites baixos para quem possuem boa de utilização

