from pessoa import funcionario
from pessoa import gerente


nome = input('Qual o seu nome? ')
cpf = input('Qual o seu cpf? ')
salario = float(input('Qual o seu sálario? R$'))
cargo = input('Qual o seu cargo? ')
horasextra = int(input('Quantas horas extra você fez? hrs: '))


funcionario1 = funcionario(nome, cpf, cargo, horasextra, salario)
print('-' * 20)
print(funcionario1.calculo_horaExtra())
print('-' * 20)





'''nomeG = input('Digite o nome do Gerente: ')
cpfG = input('Cpf do Gerente: ')
setorG = input('Setor do Gerente: ')
qtdEquip = int(input('Quantidade da equipe: '))
salarioG = float(input('Digite o salario do gerente: '))

gerente1 = gerente(nomeG, cpfG, setorG, qtdEquip, salarioG)
print('-' * 20)
print(gerente1.informacoes_gerente())
print('-' * 20)
print(f'Salario do gerente: {gerente1.salario}')
print(f'Salário do gerente com bonificação: R${gerente1.calculo_bonificação()}')
print('-' * 20)
'''



