numero =  10


# listas 
# lista vazia
listas  =  []
lista  =  [10,20,30]


print(lista)


lista[1] = 250


print(lista)



# append  remove insert count  del  pop 
# extend e se possível +=



lista =  [1,2,3,4,5,6]


lista.append(250)
print(lista) 


lista.extend([11,22,33])


print(lista) 


lista +=(10,20,30)


print(lista) 


lista.insert(0,500)


print(lista) 



# -------------------------------------------


# deletar dados



lista.remove(4)


del lista[1]
lista.pop()
lista.pop(2)



# --------------------------------


# verificar algo



print(len(lista)) # comprimento
print(max(lista)) # maior
print(min(lista)) # menor 
print(lista.count(10)) # quantos tem de alhum do valores
# print(lista.copy()) # copiar a lista 
# print(lista.clear) # limpar a lista 


print(dir(lista)) #verificar quais metodos posso usar com esse objeto
lista.sort(reverse=True) # ordenar a lista 
print(lista)
print(lista) 


l  =  list(range(1,2001))
print(l)
l =  [1,2,3,4,5,6,7,8,9,10]
lista  =  [[10,20],[10,30]]
print(lista[0][1])


#TUPLAS


# Imutavel em essencia 
# porem é possivek garregar dado com +=()
# acssamos os indices com o colchetes



lista  =  [0,30,0,30]


tupla  = (10,2,3)
t =  1,2,3,4,5,6


tup =  tuple(range(1,11))
print(tup)


tup += (10,30,10) 


# tupla.append(100)
print(tup)

dicionario =  {'key': 'value 1'}
print(dicionario['key'])


dicionario['novo'] =  'teste'



print(dicionario)



d = {


'a':10,
'b':100,
'c':250,
'e':[10,30,30,30],
'f':(10,30),
'g':{
1:10,
2:250


}



}



d  =  dict(a  = 100 , c  =  250)
print(d)





pessoa = {
'nome':'fernanda', 
'idade':20,
'endereco':'rua 65',
'livros':{


'a':'teste1',
'b':'teste2'


}



}

conjunto =  {1,2,6,6,4}
conjunto2 =  {1,20,60,60,410}


x  =  set(range(1,11))


# x  =  conjunto.difference(conjunto2)


print(x)

dicionario =  {'key': 'value 1'}
print(dicionario['key'])


dicionario['novo'] =  'teste'



print(dicionario)



d = {


'a':10,
'b':100,
'c':250,
'e':[10,30,30,30],
'f':(10,30),
'g':{
1:10,
2:250


}



}



d  =  dict(a  = 100 , c  =  250)
print(d)





pessoa = {
'nome':'fernanda', 
'idade':20,
'endereco':'rua 65',
'livros':{


'a':'teste1',
'b':'teste2'


}



}

