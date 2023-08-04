salario = float(input('Digite o salario por hora: '))
horas = float(input('Horas trabalhada no mes: '))
salario_mes = horas * salario
impostoR = salario_mes * 0.11
inss = salario_mes * 0.08
sindicato = salario_mes * 0.05

print(f'O salario bruto é de: R${salario_mes}')
print(f'Valor pago ao INSS R${inss}')
print(f'Quanto pagou ao sindicato R${sindicato}')
print(f'Descontos foram de R${sindicato + inss + impostoR}')
print(f'O salario liquido com os descontos foram de: R${salario_mes - (sindicato + inss + impostoR) } ') 