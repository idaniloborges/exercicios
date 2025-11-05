import statistics

def media(conj_dados):
    print(f'Média: {statistics.mean(conj_dados):.2f}') 

def moda(conj_dados):
    verificacao = set(conj_dados)
    if len(conj_dados) == len(verificacao):
        print(f'Não há moda: {verificacao}')
    else:
        print(f'Moda: {statistics.mode(conj_dados)}')

def mediana (conj_dados):
    print(f'Mediana: {statistics.median(conj_dados)}')


def analise_empresarial(conj_dados):

    media = statistics.mean(conj_dados)
    mediana = statistics.median(conj_dados)
    verificacao = set(conj_dados)
    variancia = statistics.variance(conj_dados)
    desvio_padrao = statistics.stdev(conj_dados)
    amplitude = max(conj_dados) - min(conj_dados)
    
    print(f'Média: {media:.2f}')
    print(f'Mediana: {mediana}')
    
    if len(conj_dados) == len(verificacao):
        print(f'Não há moda: {verificacao}')
    else:
        print(f'Moda: {statistics.mode(conj_dados)}')
    
    print(f'Variancia: {variancia:.2f}')

    print(f'Desvio padrão: {desvio_padrao:.2f}')

    print(f'Amplitude: {amplitude:.2f}')


# Desafio 2

def media(aluno):
    media_notas = statistics.mean(aluno['notas'])
    print(f'Média das notas: {media_notas}')

def mediana(aluno):
    mediana_notas = statistics.median(aluno['notas'])
    print(f'Mediana das notas: {mediana_notas}')