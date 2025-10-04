# 1. Crie um pacote chamado [calculo.py](http://calculo.py) e crie uma função para cada operação: +, -, *, /. Depois chame este pacote com o código ***import calculo*** .

    # Após chame as funções uma a uma passando os parâmetros a e b com os devidos números para operar e veja o resultado

from calculo import *

a, b = float(input('Digite um valor: ')), float(input('Digite outro valor: '))

print(f'Soma: {soma(a,b):.2f}')
print(f'Subtração: {sub(a,b):.2f}')
print(f'Multiplicação: {mult(a,b):.2f}')
print(f'Divisão: {div(a,b):.2f}')
