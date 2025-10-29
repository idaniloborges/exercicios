VENDAS = {
'SETOR1':{
'MÊS 1':[150,200,300]},
'SETOR2':{
'MÊS 2':[300,250,300]},
'SETOR3':{
'MÊS 3':[15,20,300]},
'SETOR4':{
'MÊS 4':[150,2000,300],
}
}

# Você foi contratado para verificar qual setor vendeu mais, 
# qual a media total de vendas?
# Qual a maior venda?
# Utilize as estruturas que você já conhece.




venda_setor1 = [VENDAS['SETOR1']['MÊS 1'][0], VENDAS['SETOR1']['MÊS 1'][1], VENDAS['SETOR1']['MÊS 1'][2]]
maior_v_s1= max(venda_setor1)# maior venda
soma1 = sum(venda_setor1) # soma 

print(soma1)

venda_setor2 = [VENDAS['SETOR2']['MÊS 2'][0], VENDAS['SETOR2']['MÊS 2'][1], VENDAS['SETOR2']['MÊS 2'][2]]
maior_v_s2= max(venda_setor2)
soma2 = sum(venda_setor2)

print(soma2)

venda_setor3 = [VENDAS['SETOR3']['MÊS 3'][0], VENDAS['SETOR3']['MÊS 3'][1], VENDAS['SETOR3']['MÊS 3'][2]]
maior_v_s3= max(venda_setor3)
soma3 = sum(venda_setor3)

print(soma3)

venda_setor4 = [VENDAS['SETOR4']['MÊS 4'][0], VENDAS['SETOR4']['MÊS 4'][1], VENDAS['SETOR4']['MÊS 4'][2]]
maior_v_s4= max(venda_setor4)
soma4 = sum(venda_setor4)

print(soma4)


lista_total = []
lista_total +=(soma1, soma2, soma3, soma4)
# print(lista_total)

maiores_vendas_por_setor = []
maiores_vendas_por_setor +=(maior_v_s1, maior_v_s2, maior_v_s3, maior_v_s4)
# print(maiores_vendas_por_setor)

nomes_setores =  ['SETOR1', 'SETOR2', 'SETOR3', 'SETOR4']

# TESTE =  [VENDAS['SETOR1']]
# print(TESTE)

# qual setor vendeu mais?

# mais_vendeu = sum(lista_total)
# mm = mais_vendeu  
# print('mais vendeu', mais_vendeu) 

# qual a media de vendas?
media  =  sum(lista_total)/len(lista_total)
# print('Média', media) 

# Qual a maior venda?
M = max(maiores_vendas_por_setor)
indice = maiores_vendas_por_setor.index(M)
# print('Maior venda: ', M, 'do setor', nomes_setores[indice] )


# SETOR QUE MAIS VENDEU
total_setor =  max(lista_total)
# print('SETOR QUE MAIS VENDEU',total_setor,nomes_setores[indice] )

# dicionario = {'key': 'value'}
# listas = []
# 