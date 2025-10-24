

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


print('Maior nota:')
print(max(lista_notas))


print('Menor nota: ')
print(min(lista_notas))


print('Média notas')
media  = sum(lista_notas) / len(lista_notas)
print(media)