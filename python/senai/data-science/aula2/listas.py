# lista = ['Danilo', 'Borges', 'Santos']
lista2 = [1, 2, 4]


# for nome in lista:
#     print(nome)

print(lista2[0] + lista2[1] + lista2[2])

lista2[0] = 250

print(lista2)

# append, remove, insert, count, del, pop, extend, +=, max, min

lista2.append(500)
lista2.remove(2)
lista2.extend([10, 20, 30])
lista2 += (40, 50, 60)
lista2.insert(0, 25)
lista2.pop(1)
lista2.count(20)
lista2.sort(reverse=True)
lista2.sort()

print(lista2)
print(max(lista2))
print(min(lista2))
# print(lista.copy)
# print(lista.clear())
print(sum(lista2))


l = list(range(1, 2001))
print(l)

lista = [[10,20], [30,40]]
print(lista[0][1])


# Tupla
# É possível apenas adicionar valores, mas não remover o
tupla = (10, 2, 32)

print(tupla[0])

tupla += (5, 8, 15)

print(tupla)


# Dicionário

dicionario = {'key': 'value1'}
print(dicionario['key'])

dicionario['novo'] = 'teste'
print(dicionario['novo'])

d = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 50,
    'f': [5,10,20],
    'g': (5,10,20),
    'h': {
        1: 10,
        2: 20
    }
}

print(d)


# Conjunto

conjunto = {1, 1, 5, 10, 15, 15}

