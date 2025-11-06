import statistics

# def media(conj_dados):
#     print(f'Média: {statistics.mean(conj_dados):.2f}') 
#     print('-------------')

# def moda(conj_dados):
#     verificacao = set(conj_dados)
#     if len(conj_dados) == len(verificacao):
#         print(f'Não há moda: {verificacao}')
#     else:
#         print(f'Moda: {statistics.mode(conj_dados)}')

# def mediana (conj_dados):
#     print(f'Mediana: {statistics.median(conj_dados)}')


# def analise_empresarial(conj_dados):

#     media = statistics.mean(conj_dados)
#     mediana = statistics.median(conj_dados)
#     verificacao = set(conj_dados)
#     variancia = statistics.variance(conj_dados)
#     desvio_padrao = statistics.stdev(conj_dados)
#     amplitude = max(conj_dados) - min(conj_dados)
    
#     print(f'Média: {media:.2f}')
#     print(f'Mediana: {mediana}')
    
#     if len(conj_dados) == len(verificacao):
#         print(f'Não há moda: {verificacao}')
#     else:
#         print(f'Moda: {statistics.mode(conj_dados)}')
    
#     print(f'Variancia: {variancia:.2f}')

#     print(f'Desvio padrão: {desvio_padrao:.2f}')

#     print(f'Amplitude: {amplitude:.2f}')


# Desafio 2

def media(notas):
    return statistics.mean(notas)

def mediana(notas):
    return statistics.median(notas)

def moda(notas):
    notas_ordenadas = set(notas)
    if len(notas_ordenadas) == len(notas):       
        return 'Não há moda.'
    else: 
        return statistics.mode(notas)

def desvio_padrao(notas):
    return statistics.stdev(notas)

def amplitude(notas):
    return max(notas) - min(notas)

def menor_nota(lista_alunos, notas):
    alunos_nota_menor = []
    menor_nota = min(notas)
    
    for aluno in lista_alunos:
        for nota in aluno['notas']:
            if nota == menor_nota:
                alunos_nota_menor.append(aluno["nome"])
                
    # print(alunos_nota_menor)
    print(f'-------- Alunos com a menor nota {menor_nota} --------')
    
    for aluno in alunos_nota_menor:
        print(f'- {aluno}')


def maior_nota(lista_alunos, notas):
    alunos_nota_maior = []
    maior_nota = max(notas)
    
    for aluno in lista_alunos:
        for nota in aluno['notas']:
            if nota == maior_nota:
                alunos_nota_maior.append(aluno["nome"])
                
    # print(alunos_nota_maior)
    print(f'-------- Alunos com a maior nota {maior_nota} --------')
    
    for aluno in alunos_nota_maior:
        print(f'- {aluno}')
    