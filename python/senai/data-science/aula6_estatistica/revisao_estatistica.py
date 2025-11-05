import statistics

# Média, Moda e Mediana

# # print(functions.somar(2,5))

conj_dados =[1, 25, 24, 41, 14, 55, 1]

# media = functions.media(conj_dados)
# moda = functions.moda(conj_dados)
# mediana = functions.mediana(conj_dados)

# print(media)
# print(moda)
# print(mediana)


# Variancia, Amplitude, Desvio padrão

variancia = statistics.variance(conj_dados)
d_padrao = statistics.stdev(conj_dados)
amplitude = max(conj_dados) - min(conj_dados)


print(f'Variancia: {variancia:.2f}')
print(f'Desvio padrão: {d_padrao:.2f}')
print(f'Amplitude: {amplitude}')

print(d_padrao**2 == variancia)