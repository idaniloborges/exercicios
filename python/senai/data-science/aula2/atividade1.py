# Você foi contratado para analisar o desempenho de um grupo de alunos em uma disciplina, 
# você vai analisar apenas pela média. 
# As notas de cada aluno em diferentes provas estão armazenadas em listas. O
#  objetivo é usar listas bidimensionais para representar as notas de cada aluno e 
# realizar algumas análises básicas, como:

# ***Calcular a média das notas de cada aluno.
# Identificar o aluno com a maior média.*
# Calcular a média da classe (média geral de todos)**



# contador = 0
# aluno_media_maior = ''
# maior_media = 0
# media_geral = 0

# for aluno in nomes:
#     print({aluno: notas[contador]})

#     media = sum(notas[contador]) / len(notas[contador])
#     print(f'Média das notas: {media:.2f}')

#     media_geral += media
#     print(f'Média geral da turma: {media_geral / len(nomes)}')
    
#     if media > maior_media:
#         maior_media = media
#         aluno_media_maior = aluno
    
#     print(f'Maior média: {aluno_media_maior, maior_media}')
    
#     contador += 1
    # print(contador)
# print((30+10+22+16)/(4*3))

# SEM LOOPS E CONDIÇÕES

nomes = ['Ana','Fernanda', 'Caio', 'Fernando']
notas = [[10,10,10],[5,2,3],[5,9,8],[10,0,6]]

# alunos = {
#     nomes[0]: notas[0],
#     nomes[1]: notas[1],
#     nomes[2]: notas[2],
#     nomes[3]: notas[3],
# }

# print(alunos)

# aluno_media1 = alunos[nomes[0]]
# print(alunos[nomes[0]])
# print(f'{alunos[nomes[0]]}: {aluno_media1}')


# ***Calcular a média das notas de cada aluno.
# Identificar o aluno com a maior média.*
# Calcular a média da classe (média geral de todos)**


aluno1 = [nomes[0], sum(notas[0]) / 3]
aluno2 = [nomes[1], sum(notas[1]) / 3]
aluno3 = [nomes[2], sum(notas[2]) / 3]
aluno4 = [nomes[0], sum(notas[3]) / 3]


media_geral = (aluno1[1] + aluno2[1] + aluno3[1] + aluno4[1]) / 4
maior_media1 = max(aluno1[1], aluno2[1], aluno3[1], aluno4[1])

print(f'Média {aluno1[0] : aluno1[1]}')

print(f'Média geral: {media_geral}')
print(f'Maior média: {maior_media1}')
