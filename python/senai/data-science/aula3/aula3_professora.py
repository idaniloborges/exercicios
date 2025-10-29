import random


print('CADASTRE-SE PRIMEIRO PARA ACESSAR O SISTEMA')

dados  =  {'login':[], 'senha':[]}

login  =  input('login: ')
senha  =  input('Senha: ')

dados['login'].append(login)
dados['senha'].append(senha)

print('dados salvos com sucesso...')

senha_dig = input('Digite a senha para acessar: ')
login_dig = input('Login: ')

if senha_dig in dados['senha'] and login_dig in dados['login']:
    print('Seja bem vindo(a) site de jogos')
    print('ESCOLHA O SEU JOGO:')
    print()
    escolha_usuario  =  input('''
                      
    1 - jogo da advinhação
    2 - jogo pedra papel tesoura
    3 - adivinhe a palavra                 

''')
    
    if escolha_usuario == '1':
    
        numero_aleatorio =  random.randint(1,10)
        meu_chute = int(input('chute: '))
        if meu_chute == numero_aleatorio:
            print('Acertou em cheio!O número é: ', numero_aleatorio)
        else:
            print('Errou feio!O número é: ', numero_aleatorio)     
    elif escolha_usuario  == '2':
         lista  =  ['pedra','papel', 'tesoura']
         escolha_maq  = random.choice(lista)
         user_esc = input(f'Digie a sua opção: {lista}')
         if escolha_maq == user_esc:
             print('EMPATE!')
         elif escolha_maq == 'pedra' and user_esc == 'tesoura':
             print('O computador ganhou')
         elif escolha_maq == 'papel' and user_esc == 'pedra':
             print('O computador ganhou')                  
         elif escolha_maq == 'tesoura' and user_esc == 'papel':
             print('O computador ganhou')

         elif escolha_maq == 'tesoura' and user_esc == 'pedra':
             print('Você gahou!')
         elif escolha_maq == 'pedra' and user_esc == 'paple':
             print('Você gahou!')                  
         elif escolha_maq == 'papel' and user_esc == 'tesoura':
             print('Você gahou!')

         else:
             print('Digite algo válido')
    elif escolha_usuario == '3':
         print('Associe a palavra')
         charadas =  ['Quanto mais se tira, maior fica?','Tem dente, mas não morde?','Tem chaves, mas não abre portas?' ]             
         respostas =  ['buraco','pente','teclado']

         perg_aleatoria = random.choice(charadas)
         print('RESPONDA: ', perg_aleatoria)
         id_user = int(input(f'''
         digite o id da respostas      
         0 {respostas[0]} 
         1 {respostas[1]}
         2 {respostas[2]}

'''))
         indice = charadas.index(perg_aleatoria)
         if indice == id_user:
             print('Acertou!' )
         else:
             print('Errou')   

         
         

else:
    print('Digite novamente...')    
