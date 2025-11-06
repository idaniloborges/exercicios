import statistics


def analise(notas):
    media  =  statistics.mean(notas)
    moda = statistics.mode(notas)
    mediana =  statistics.median(notas)
    desvio =  statistics.stdev(notas)
    amplitude  =  max(notas) -  min(notas)

    print(f'''
          

          MEDIA      - {media}     
          MODA       - {moda}      
          MEDIANA    - {mediana}   
          AMPLITUDE  - {amplitude} 
          DESVIO     - {desvio}    


         ''')

def maior_nota(notas):
    maior =  max(notas)
    print('Maior notas:', maior)

def menor_nota(notas):
    menor =  min(notas)
    print('Menor nota: ', menor)

