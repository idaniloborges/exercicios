# Você é um Dev Jr. e precisa criar um sistema de coletas de dados. 
# Utilize as condicionais, para escolher o  métodos de lista  para:
# Utilize  -  if else elif , funções built de manipulação de listas
# não utilize funções e loops
# Exemplo: 


# espaço na memória que cabe mais dados


dados = [10,20,30,10]
escolha  =  input('''
                  
1 - Mostra o dado
2 - Alterar o dado
3 - Coletando Dados de Experimentos
4 - Analisando a Soma de Dados de Vendas
5 - Localizar um Registro no Conjunto de Dados


''')



if escolha == '1':
    print('DADOS COLETADOS: ')
    print(dados)
elif escolha == '2':
    print('dados', dados)
    dado_velho = int(input('Qual dado você deseja alterar? '))
    novo_dado = int(input('Digite o novo dado:  '))
    indice =  dados.index(dado_velho)
    dados[indice] = novo_dado
    print('DADOS:', dados)
elif escolha  == '3':   
    dados.extend([int(input('novo dado 1: ')),int(input('novo dado 1: '))])
    print('Lista atualizada: ', dados) 
elif escolha == '4':
    soma  =  sum(dados)
    print('Total:', soma)
elif escolha =='5':
    print('dados: ',dados) 
    registro = int(input('Busque o dado: '))
    if registro in dados:
        print('existe na lista')
        posicao =  dados.index(registro)
        print('Posição:', posicao)
    else:
        print('Não existe na lista') 
else:
    print('Digite algo válido!')           



