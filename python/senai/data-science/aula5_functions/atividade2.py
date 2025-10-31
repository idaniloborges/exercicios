# 2 - Com funções crie um sistema de para calcular o IMC


def imc():
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

    imc = peso / altura**2

    if imc < 0:
        print("Digite valores válidos")

    elif imc >= 0 and imc < 16:
        print("Situação: Magreza grave")

    elif imc < 17:
        print("Situação: Magreza moderada")

    elif imc < 18.5:
        print("Situação: Magreza leve")

    elif imc < 25:
        print("Situação: Saudável")

    elif imc < 30:
        print("Situação: Sobrepeso")

    elif imc < 35:
        print("Situação: Obesidade grau l")

    elif imc < 40:
        print("Situação: Obesidade grau ll")

    elif imc > 40:
        print("Situação: Obesidade grau lll")

    print(f"Seu IMC é: {imc:.2f}")


imc()
