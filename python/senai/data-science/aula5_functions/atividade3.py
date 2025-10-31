# 3 - Com funções crie um jogo da adivinhação
import random


def advinhar():
    sorteio = random.randint(0, 10)
    tentativa = int(input("Escolha um número (0~10): "))
    while tentativa != sorteio:
        print(f"Número sorteado: {sorteio}")
        print(f"Número escolhido: {tentativa}")
        print("Você errou! Tente novamente.")
        print("-------------------------------")
        tentativa = int(input("Escolha um número (0 ~ 10): "))
        sorteio = random.randint(0, 10)

    print(f"Número sorteado: {sorteio}")
    print(f"Número escolhido: {tentativa}")
    print(f"Você acertou!")
    print("-------------------------------")


advinhar()
