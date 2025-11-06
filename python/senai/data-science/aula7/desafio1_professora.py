import statistics


def analise(salarios, f):

    media  =  statistics.mean(salarios)
    moda = statistics.mode(salarios)
    mediana =  statistics.median(salarios)
    desvio =  statistics.stdev(salarios)
    amplitude  =  max(salarios) -  min(salarios)
    variancia  =  statistics.variance(salarios)
   
    i =  f.index(salarios)

    print(f'''
          MEDIA      - {media}     empresa - {i}
          MODA       - {moda}      empresa - {i}
          MEDIANA    - {mediana}   empresa - {i}
          AMPLITUDE  - {amplitude} empresa - {i}
          DESVIO     - {desvio}    empresa - {i}
          VARIANCIA  - {variancia} empresa - {i}

         ''')


empresa1 = [2500, 2800, 3000, 9500, 12000]
empresa2 = [5000, 5200, 5300, 5400, 5500]
empresa3 = [1000, 2000, 8000, 15000, 20000]
empresa4 = [3500, 4000, 4200, 4300, 6000]
empresa5 = [1200, 1500, 1800, 2500, 10000]

empresas  =  ['', empresa1,empresa2, empresa3,empresa4, empresa5]

analise(empresa1, empresas)
analise(empresa2, empresas)
analise(empresa3, empresas)
analise(empresa4, empresas)
analise(empresa5, empresas)