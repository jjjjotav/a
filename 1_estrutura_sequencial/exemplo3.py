peso = float(input('Digite o peso do peixe: kg'))
multa = (peso - 50) * 4

if peso > 50:
    print(f'O peso do peixe é {peso}kg e excedeu o peso regulamentado')
    print(f'Valor a pagar em multa é de R${multa}')
else:
    print('Peixe não excedeu o peso regulamentado')

