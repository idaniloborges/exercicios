
print('CADASTRE-SE PRIMEIRO PARA ACESSAR O SISTEMA')

dados  =  {'login':['@bea'], 'senha':['123']}

print('dados salvos com sucesso...')

senha_dig = input('Digite a senha para acessar: ')
login_dig = input('Login: ')

if senha_dig in dados['senha'][0] and login_dig in dados['login'][0]:
    print('BEM VINDO(A) AO E-COMMERCE X')
    produtos  =  ['', 'PRODUTO A', 'PRODUTO B', 'PRODUTO C']
    valores  =  [0,100.0,250.55,300.25]
    print(produtos)

    carrinho  = [] 
    meu_total = []
    
    prod_1 = int(input('Digite o id do produto -  1 , 2, 3'))
    prod_2 = int(input('Digite o id do produto -  1 , 2, 3'))
    prod_3 = int(input('Digite o id do produto -  1 , 2, 3'))

    carrinho.extend([produtos[prod_1], produtos[prod_2], produtos[prod_3]])
    meu_total.extend([valores[prod_1], valores[prod_2], valores[prod_3]])
    soma   = sum(meu_total) 
    print('Produtos', carrinho)
    print(f'R$, {soma:.2f}')

    formapag = ['','1 PIX','2 CC','3 CD']
    escolha_pag = int(input(f'Escolha a forma de pagamento{formapag}'))
    print('Sua forma de pagamento é', formapag[escolha_pag])





else:
    print('Algo deu errado')    