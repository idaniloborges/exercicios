import random

dados = {'login': [], 'senha': []}

login = input('login: ')
senha = input('Senha: ')

dados['login'].append(login)
dados['senha'].append(senha)

print('dados salvos com sucesso...')

print(dados)


login_dig = input('Digite o login para acessar: ')
senha_dig = input('Digite a senha para acessar: ')

if login_dig in dados['login'] and senha_dig in dados['senha']:
    print('Seja bem vindo!')
    numero_aleatorio = random.randint(1, 10)
    palpite = int(input('Digite um numero: '))
    if palpite == numero_aleatorio:
        print(f'Acertou, o número é {numero_aleatorio}')
    else:
        print('Errou')
else:
    print('Tente novamente...')