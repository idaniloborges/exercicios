# saque
saldo = 5000

saque = float(input('saque: '))
saldo = saldo - saque

print(f'Em conta: R${saldo:.2f}')

# deposito
deposito = float(input('deposito: '))
saldo = saldo + deposito

print(f'Em conta: R${saldo:.2f}')

# extrato
print(f'OPERAÇÃO SAQUE {saque:.2f}')
print(f'OPERAÇÃO DEPÓSITO {deposito:.2f}')
print(f'SALDO EM CONTA {saldo:.2f}')


