tabuada = 0

while tabuada < 1 or tabuada > 10:
        tabuada= int(input("Digite um numero: "))
for numero in range(1, 11):
    resultado = tabuada * numero
    print(f"{tabuada} * {numero} = {resultado}")
    


