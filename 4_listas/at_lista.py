#Faça um algoritimo que leia 20 numeros inteiro
#e armazene-os numa lista. armazene os numeros
#pares na lista pares e os impares na lista impares imprima as tres listas

lista = []
impar = []
par = []

for i in range(1, 21):
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
        

print(f"Todos os numeros: {lista}")
print(f"Impares: {impar}")
print(f"pares: {par}")
    