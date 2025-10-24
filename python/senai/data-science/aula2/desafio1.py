# Desafio 1
# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA.
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE AS NOTAS DE ALUNOS, MÉDIA, 
# ALÉM DE MOSTRAR MENOR E A MAIOR NOTA.
# lista, tuplas, dicionarios, conjunto
# input() print() sinais ariméricos, funções das estruturas compostas 

notas = [5.8, 9, 10, 6.9, 7, 8.3]

menor_nota = min(notas)
maior_nota = max(notas)
media = sum(notas) / len(notas)

print(f'Notas: {notas}')
print(f'Menor nota: {menor_nota:.2f}')
print(f'Maior nota: {maior_nota:.2f}')
print(f'Média: {media:.2f}')
