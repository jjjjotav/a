def soma(numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total
    
def maior(numeros):
    maior = 0
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

resultado1 = soma([1, 2, 3, 4])
resultado2 = soma([2, 14, 11, 5, 6, 7, 8, 9, 10,])
maior1 = maior([1, 2, 3, 4])
maior2 = maior([2, 14, 11, 5, 6, 7, 8, 9 , 10])

print(f"Resultado1: {resultado1}")
print(f"resultado2: {resultado2}")

print(f"Maior1: {maior1}")
print(f"Maior2: {maior2}")
