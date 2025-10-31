# calculadora


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def calculadora():
    # number1 = float(input('Digite o primeiro valor: '))
    op = input("Digite a operação: ")
    # number2 = float(input('Digite o segundo valor: '))

    if op == "+":
        n1 = float(input("="))
        n2 = float(input("="))
        print(f"Soma: {soma(n1,n2)}")

    if op == "-":
        n1 = float(input("="))
        n2 = float(input("="))
        print(f"Subtração: {subtracao(n1,n2)}")

    if op == "*":
        n1 = float(input("="))
        n2 = float(input("="))
        print(f"Multiplicação: {multiplicacao(n1,n2)}")

    if op == "/":
        n1 = float(input("="))
        n2 = float(input("="))
        print(f"Divisão: {divisao(n1,n2)}")


# calculadora()


def verificar_indice(num, lista):
    indice = lista.index(num)
    print(f"índice: {indice}")
    print(f"Número: {num}")


lista = [10, 20, 30]

n = int(input("number: "))

verificar_indice(n, lista)
