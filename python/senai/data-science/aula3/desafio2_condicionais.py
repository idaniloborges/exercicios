# - ***Desafio 2  Condicionais***

# ***Você é um Dev Jr. e precisa criar um sistema de coletas de dados.*** 

# ***Utilize as condicionais, para escolher o tipo de dado e os métodos de lista*** 

# ***para:***

# Utilize if else elif, funções de manipulações de listas

# Exemplo: 

# - ***Mostra o dado;***
# - ***Alterar o dado;***
# - ***Coletando Dados de Experimentos***
# - ***Analisando a Soma de Dados de Vendas***
# - ***Localizar um Registro no Conjunto de Dados***

dados = [10,20,30,10]

opcao_geral = int(input('''Escolha uma opção: 
1 - Mostra o dado
2 - Alterar o dado
3 - Coletando Dados de Experimentos
4 - Analisando a Soma de Dados de Vendas
5 - Localizar um Registro no Conjunto de Dados
Opção: '''))

if opcao_geral == 1:
    print(f'Dados: {dados}')
elif opcao_geral == 2:
    escolher_posicao = int(input('Escolha a posição do dado: '))
    if escolher_posicao >= 0 and escolher_posicao <= len(dados):
        alterar_dado = int(input('Escolha o novo valor: '))
        dados[escolher_posicao] = alterar_dado
        print('Dados alterados!')
        print(f'Dados atualizados: {dados}')
    else:
        print('Valor inválido! Tente novamente...')
elif opcao_geral == 3:
    novo_dado = input('Informe o dado a ser adicionado: ')
    if novo_dado.isdigit():
        dados.append(float(novo_dado))
        print('Dado adicionado!')
        print(f'Dados atualizados: {dados}')
    else:
        print('Error. Digite um dado tipo número.')
elif opcao_geral == 4:
    print(f'Total geral R$: {sum(dados):.2f}')
    print(f'Maior venda R$: {max(dados):.2f}')
    print(f'Menor venda R$: {min(dados):.2f}')
elif opcao_geral == 5:
    posicao = int(input('Digite a posição do dado: '))
    if posicao >= 0 and posicao <= len(dados):
        print(f'Registro: {dados[posicao]}')
    else:
        print('Error. Posição fora do range')