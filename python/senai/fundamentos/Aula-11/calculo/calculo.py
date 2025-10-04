# 1. Crie um pacote chamado [calculo.py](http://calculo.py) e crie uma função para cada operação: +, -, *, /. Depois chame este pacote com o código ***import calculo*** .

    # Após chame as funções uma a uma passando os parâmetros a e b com os devidos números para operar e veja o resultado

def soma(a,b):
  return a + b

def sub(a,b):
  return a - b

def mult(a,b):
  return a * b

def div(a,b):
  return a / b

if __name__ == "__main__":
  a=1
  b=3
  print(soma(5,6))
  print(sub(a,b))
  print(mult(a,b))
  print(div(a,b))

