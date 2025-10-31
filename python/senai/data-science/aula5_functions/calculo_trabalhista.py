# SISTEMA DE CALCULO TRABALHISTA

# 1- HORA NORMAL
def cal_val_hr(carga, salario):
    return salario / carga

# 2 - HORA EXTRA
def hora_extra(valor_hora):
    return valor_hora * 1.5

# 3 - QUANTAS HORAS EXTRAS REALIZADAS
def quantidade_extra(quantidade, valor_hr_extra):
    return quantidade * valor_hr_extra

# 4 - TOTAL SALARIO
def sal(total_extra, salario):
    return total_extra + salario

def sistema():
    salario = float(input('Salario: '))
    quantidade_ex = float(input('Hora extra: '))
    carga = float(input('Carga: '))

    valor_hora = cal_val_hr(carga, salario)
    print(f'Valor hora R$ {valor_hora:.2f}')
    print('-------------------')

    extra = hora_extra(valor_hora)
    print(f'VALOR DA HORA EXTRA R$ {extra:.2f}')

    print('-------------------')
    quantidade_ = quantidade_extra(quantidade_ex, extra)
    print(f'TOTAL HORA EXTRA R$ {quantidade_:.2f}')

    print('-------------------')
    salario_t = sal(quantidade_, salario)
    print(f'SALARIO TOTAL R$ {salario_t:.2f}')

sistema()
