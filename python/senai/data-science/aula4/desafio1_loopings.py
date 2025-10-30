# 1 - Crie um sistema de banco, com as seguintes operações:
# COM LOOPS - CONDICIONAIS  -  VARIÁVEIS -  LISTAS - DICIONÁRIOS. 

# # SISTEMA DE BANCO 

# - Acesso a conta
# (CONDICIONAL COMPARAR) Ver extrato
# (PRINT(SALDO))
# - Fazer um deposito
# (SOMA -  VALOR SALDO + DEPOSITO(FLOAT))
# - Fazer um saque 
# (SUBTRAÇÃO -  SALDO - SAQUE(FLOAT))
# - Sair do sistema 
# (DESPEDIR)

dados  =  {'login':['1'], 'senha':['1']}

extrato = []
saldo = sum(extrato)

login_dig = input('Login: ')
senha_dig = input('Digite a senha para acessar: ')

if login_dig in dados['login'] and senha_dig in dados['senha']:

        opcao = input('''
1 - Ver extrato
2 - Ver saldo
3 - Fazer um depósito
4 - Fazer um saque
5 - Sair do sistema
Digite sua opção: ''')


        while opcao != '5':
            if opcao == '1':
                if extrato == []:
                    print('Não há histórico de transação.')
                    opcao = input('''
1 - Ver extrato
2 - Ver saldo
3 - Fazer um depósito
4 - Fazer um saque
5 - Sair do sistema
Digite sua opção: ''')  
                else:
                    print(f'Extrato: {extrato}')
                    opcao = input('''
1 - Ver extrato
2 - Ver saldo
3 - Fazer um depósito
4 - Fazer um saque
5 - Sair do sistema
Digite sua opção: ''')
            elif opcao == '2':
                 print(f'Saldo: R${sum(extrato):.2f}')
                 opcao = input('''
1 - Ver extrato
2 - Ver saldo
3 - Fazer um depósito
4 - Fazer um saque
5 - Sair do sistema
Digite sua opção: ''')
            elif opcao == '3':
                deposito = float(input('Digite o valor a ser depositado: '))
                extrato.append(deposito)
                opcao_deposito = input('Deseja fazer outro depósito?')
                while opcao_deposito == 'sim':
                        deposito = float(input('Digite o valor a ser depositado: '))
                        extrato.append(deposito)
                        # saldo = sum(extrato)
                        print(f'Saldo: R${saldo:.2f}')
                        opcao_deposito = input('Deseja fazer outro depósito?')             
                else:
                     opcao = input('''
1 - Ver extrato
2 - Ver saldo
3 - Fazer um depósito
4 - Fazer um saque
5 - Sair do sistema
Digite sua opção: ''')
            elif opcao == '4':
                saque = float(input('Digite o valor a ser sacado: '))
                # saldo = sum(extrato)
                if saque > saldo:
                    print('Saldo insuficiente...')
                    saque = float(input('Digite o valor a ser sacado: '))
                else:
                    extrato.append(-(saque))
                    # saldo = sum(extrato)
                    # print(saldo-saque)
                    print(f'O novo saldo é: R${saldo:.2f}')
                    print('--------------')
                    opcao = input('''
1 - Ver extrato
2 - Ver saldo
3 - Fazer um depósito
4 - Fazer um saque
5 - Sair do sistema
Digite sua opção: ''')
            else:
                print('Digite um valor válido.')
                opcao = input('''
1 - Ver extrato
2 - Ver saldo
3 - Fazer um depósito
4 - Fazer um saque
5 - Sair do sistema
Digite sua opção: ''')
        print('Saindo...')
# print('Tente novamente...')