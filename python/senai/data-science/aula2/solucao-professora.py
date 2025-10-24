# dados primitivos em python
# variáveis
# input / output
# comentários
# sinais aritméticos
# sinais lógicos
# concatenação
#extrato**
saldo = 5000.00

#saque***
saque =  float(input('saque (-): '))
saldo =  saldo - saque
print('Em conta R$', saldo)
#deposita***
deposito =  float(input('Deposito (+): '))
saldo  =  saldo +  deposito
print('Em conta R$,{saldo:.2f}')
#saldo***
print('Saldo em conta R$:', )

# extrato:
print('OPERAÇÃO SAQUE -------- (-)',round(saque,2) )
print('OPERAÇÃO DEPOSITO ------ (+)',round(deposito,00) )
print('OPERAÇÃO SALDO EM CONTA -------- R$',round(saldo,2) )
