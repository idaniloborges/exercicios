# ## ***Desafio 2***

 

# ***VOCÊ É UM DESENVOLVEDOR E PRECISA IMPLEMENTAR UM SISTEMA PARA UMA INSTITUIÇÃO DE ENSINO.***

# ***O SISTEMA DEVE GERENCIAR AS NOTAS DOS ESTUDANTES, APRESENTANDO ESTATÍSTICAS COMO MODA, MÉDIA, MEDIANA, AMPLITUDE DESVIO PADRÃO. 
# ALÉM DISSO, DEVE IDENTIFICAR A MENOR E A MAIOR NOTA. ORGANIZE O CÓDIGO EM MÓDULOS E SEPARE AS FUNCIONALIDADES EM FUNÇÕES DISTINTAS.***

# ***1 - USAR STATISTICS***

# ***2 - UTILIZE MÓDULOS SEPARADOS***

# ***3 - Utilize Parâmetros, caso deixe mais flexível***

# 4 - Extraia os dados de todos os alunos

import statistics
import functions

lista_alunos = [
    {
    'nome': 'João',
    'notas': [4,6,8,7]
    },
    {
    'nome': 'Maria',
    'notas': [8,7,8,9]
    },
    {
    'nome': 'Isaías',
    'notas': [8,4,8,7]
    },
    {
    'nome': 'Pedro',
    'notas': [7,6,6,5]
    },
    {
    'nome': 'Abimeleque',
    'notas': [8,6,8,7]
    },
]

media_geral = []

for aluno in lista_alunos:
    print(aluno['nome'])
    functions.media(aluno)
    functions.mediana(aluno)
    
# print(statistics.mean(lista_alunos[0]['notas']))