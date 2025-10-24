# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 


# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE AS NOTAS DE ALUNOS, MÉDIA,  ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA.


# - lista, tuplas, dicionarios, conjunto
# - input() print() sinais ariméricos, funções das estruturas compostas




print('SISTEMA DE NOTAS: ')


nome1  =  input('Aluno: ')
n1 =  float(input('nota  1: '))


nome2  =  input('Aluno: ')
n2 =  float(input('nota  2: '))


nome3  =  input('Aluno: ')
n3 =  float(input('nota  3: '))


nome4  =  input('Aluno: ')
n4 =  float(input('nota  4: '))


lista_notas  = []


lista_notas.extend([n1, n2, n3, n4])


lista_nomes = []
lista_nomes.extend([nome1,nome2, nome3, nome4])


print('Maior nota:')
print(max(lista_notas))
maior = max(lista_notas)
indice =  lista_notas.index(maior)
print(indice)
print('Aluno com maior nota', lista_nomes[indice])



print('Menor nota: ')
print(min(lista_notas))


print('Média notas')
media  = sum(lista_notas) / len(lista_notas)
print(media)