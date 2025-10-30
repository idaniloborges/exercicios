# 2 - # Controle de Estoque

# Crie um sistema para controle de estoque de uma loja, onde:
# O sistema pode adicionar novos produtos com nome, quantidade e preço.
# O sistema pode vender um produto, reduzindo sua quantidade no estoque.
# O sistema pode listar todos os produtos em estoque.
# O sistema deve garantir que a quantidade de um produto não seja negativa.

# Escolha uma opção:
# 1. Adicionar produto
# 2. Vender produto
# 3. Ver estoque
# 4. Sair


# Informe o nome do produto: Arroz
# Informe a quantidade: 100
# Informe o preço unitário: 5.0

# Escolha uma opção:
# 1. Adicionar produto
# 2. Vender produto
# 3. Ver estoque
# 4. Sair

# Informe o nome do produto a ser vendido: Arroz
# Informe a quantidade a ser vendida: 10
# Venda realizada! Quantidade de Arroz em estoque: 90

# Estoque:
# - Arroz: 90 unidades, R$ 5.00 cada

estoque_produtos = []

opcao = int(input('''Escolha a opção:
# 1. Adicionar produto
# 2. Vender produto
# 3. Ver estoque
# 4. Sair 
# '''))

while opcao != 4:
    if opcao == 1:
        produto = input('Digite o nome do produto a ser adicionado: ')
        quantidade = input('Digite a quantidade: ')
        preco = input('Digite o preço unitário: ')
        estoque_produtos.append({produto:{
            'quantidade': quantidade,
            'preco': preco
        }})
        print(estoque_produtos)






estoque_produtos.append(produto)

print(lista_produtos)

