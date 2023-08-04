
from retangulo import retangulo
from circulo import circulo


retangulo1 = retangulo()
print(retangulo1.Areaa())
print('Calculando a area do retangulo')
retangulo1.base = float(input('Digite o valor da base: '))
retangulo1.altura = float(input('Digite o valor da altura: '))

print(retangulo1.AreaRetangulo())

circulo1 = circulo()
print(circulo1.Areaa())
print('Calculando a area do circulo')
circulo1.raio = float(input('Digite o valor da raio: '))
print(circulo1.AreaCirculo())