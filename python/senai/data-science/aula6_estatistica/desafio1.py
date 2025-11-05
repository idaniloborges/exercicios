# ## Desafio 1

# ***Você é um profissional em transição de carreira e está avaliando novas oportunidades de emprego.***

# ***Utilize estatísticas como média, moda, mediana e desvio padrão, amplitude, variância para analisar as faixas salariais oferecidas por diferentes empresas e tomar uma decisão embasada.***

# ***Explique sua escolha com base nos dados analisados***

# ***Verifique isso através dos salários:***

import functions
import statistics

lista_empresas = [[2500, 2800, 3000, 9500, 12000],[5000, 5200, 5300, 5400, 5500],[1000, 2000, 8000, 15000, 20000],[3500, 4000, 4200, 4300, 6000],[1200, 1500, 1800, 2500, 10000]]
lista_media = []
lista_desvio = []
lista_amplitude = []



for empresa in lista_empresas:
    print(f'-------- EMPRESA {lista_empresas.index(empresa)+1} --------')
    functions.analise_empresarial(empresa)
    lista_media.append(statistics.mean(empresa))
    lista_desvio.append(statistics.stdev(empresa))
    lista_amplitude.append(max(empresa)- min(empresa))

print('---------------------------------------------------')

print(f'Maior média salarial: R${max(lista_media):.2f} - Empresa {lista_media.index(max(lista_media))+1}')
print(f'Menor desvio padrão salarial: R${min(lista_desvio):.2f} - Empresa {lista_desvio.index(min(lista_desvio))+1}')
print(f'Maior desvio padrão salarial: R${max(lista_desvio):.2f} - Empresa {lista_desvio.index(max(lista_desvio))+1}')
print(f'Menor amplitude salarial: R${min(lista_amplitude)} - Empresa {lista_amplitude.index(min(lista_amplitude))+1}')
print(f'Maior amplitude salarial: R${max(lista_amplitude)} - Empresa {lista_amplitude.index(max(lista_amplitude))+1}')

print('---------------------------------------------------')


# Qual empresa escolheria?
# Porquê?
# O que você entendeu do desvio padrão, média, moda, mediana, amplitude,  variância dessa empresa? 

# Resposta:

    # Para estabilidade financeira, a EMPRESA 2 tem a menor amplitude, desvio padrão e uma boa média salarial.
    # Para maior crescimento de salário, a EMPRESA 3 tem a maior média salarial e a maior amplitude entre a amplitude salarial e a média (19000 - 9200)..
