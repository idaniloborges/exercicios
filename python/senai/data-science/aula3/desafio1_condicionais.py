# - ***Desafio 1 Condicionais***

# ***Crie um sistema de e-commerce, onde o usuário possa:***

# - ***cadastrar-se***
# - ***comprar um produto***
# - ***descobrir o valor total***
# - ***pagar***

dados = { 'login': [], 'senha': []}

# login = input('Escolha seu usuário: ')
# senha = input('Escolha sua senha: ')

# dados['login'].append(login)
# dados['senha'].append(senha)

# produtos = {'produto': ['banana', 'uva', 'maça'], 'preco': [5.90, 8.90, 12.90]}

produtos = ['banana', 'uva', 'maça']
preco = [5.90, 8.90, 12.90]
carrinho = []

# print(produtos['produto'])

produto_escolhido = input(f'''Escolha um produto da lista: {produtos}
: ''')

preco_produto = preco[produtos.index(produto_escolhido)]

if produto_escolhido in produtos:
    print(f'''O produto escolhido foi: {produto_escolhido}: Preço: R${preco_produto:.2f}''')
    adicionar_carrinho = input('''Deseja adicionar o produto ao carrinho? 
    1 - Sim / 2 - Não
    Escolha: ''')
    if adicionar_carrinho == '1':
        # carrinho.append({produto_escolhido: preco_produto})
        print('Produto adicionado ao carrinho...')
        pagamento = input('''Deseja realizar o pagamento agora?
        1 - Sim / 2 - Não
        Escolha: ''')
        if pagamento == '1':
            print(f'''Total da compra R$: {preco_produto:.2f}''')
            opcao_pagamento = input('''Escolha a opção de pagamento:
            1 - Pix
            2 - Cartão de crédito
            3 - Cartão de débito
            ''')
            if opcao_pagamento == '1' or opcao_pagamento == '2' or opcao_pagamento =='3':
                print('''Compra aprovada! Volte Sempre!''')
                
            else:
                print('''Compra não aprovada. Tente novamente mais tarde...''')
                
        else:
            print('''Error 404. Tente novamente mais tarde...''')
            

    elif adicionar_carrinho == '2':
        print('''Error 404.  Tente novamente mais tarde...''')  
         
else:
    print('O produto escolhido não está na lista')