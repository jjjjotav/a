maior = float('-inf')
for item in range(5):
    numero = int(input(f'Digite o numero {item + 1}: '))
    if numero > maior:
        maior = numero
    print(f"O maior numero foi {maior}. ")
