# 1 - Com funções crie um sistema de médias notas escolares

lista_notas = []


def media():

    aluno = input("Digite o nome do aluno: ")
    while aluno != "stop":
        nota1 = float(input("Digite sua primeira nota: "))
        nota2 = float(input("Digite sua primeira nota: "))
        nota3 = float(input("Digite sua primeira nota: "))
        nota4 = float(input("Digite sua primeira nota: "))

        lista_notas.append({aluno: [nota1, nota2, nota3, nota4]})

        print(lista_notas)

        aluno = input("Digite o nome do aluno: ")

    print(f'Fim')

    # media = (nota1 + nota2 + nota3 + nota4) / 4

    # if media < 0:
    #     print("Digite valores válidos.")
    # elif media > 0 and media < 7:
    #     print("----------------")
    #     print("Aluno reprovado.")
    # elif media >= 7:
    #     print("----------------")
    #     print("Aluno aprovado!")
    # print(f"A média das notas é: {media:.2f}")
    # print("----------------")


media()
